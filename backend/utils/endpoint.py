import re

from  django.db import IntegrityError
from django.http import HttpResponse, HttpResponseForbidden, HttpResponseNotModified, HttpResponseBadRequest
from itsdangerous import JSONWebSignatureSerializer, BadSignature

from backend.models import *
from backend.utils import notifier
from eventloggr.settings import DEBUG


def sanitize(inp):
    pattern = re.compile('[\W_]+')
    return pattern.sub('', inp)


def error(text, c=HttpResponseForbidden):
    if (DEBUG):
        return c(text)
    else:
        return c()


def push(request, target):
    target = sanitize(target)
    resp = "Pushing to {} ...\n".format(target)

    try:
        endpoint = Endpoint.objects.get(url=target)
    except Endpoint.DoesNotExist:
        resp += 'ERROR: target does not exist.'
        return error(resp)

    if 'data' not in request.POST:
        resp += 'ERROR: no data found in request.'
        return error(resp)

    serializer = JSONWebSignatureSerializer(endpoint.secret)
    try:
        data = serializer.loads(request.POST['data'])
    except BadSignature:
        resp += 'ERROR: bad signature.'
        return error(resp)

    if 'identifier' not in data or 'source' not in data or 'text' not in data:
        resp += 'ERROR: not all fields present in data.'
        return error(resp, HttpResponseBadRequest)

    # TODO: further input sanitization (although trusted)?

    line = Logline(service=endpoint.service,
                   identifier=data['identifier'],
                   source=data['source'],
                   text=data['text'])

    try:
        line.save()
    except IntegrityError:
        return HttpResponseNotModified()

    notifier.notify(endpoint.service, line)

    return HttpResponse('OK')
