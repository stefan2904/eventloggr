import requests
from itsdangerous import JSONWebSignatureSerializer


def notify(service, line):
    data = {'service': line.service.name,
            'source': line.source,
            'text': line.text}

    for notifier in service.notifier_set.all():
        sendNotification(notifier.url, notifier.secret, data)
        notifier.last = line.id
        notifier.save()


def sendNotification(url, secret, data):
    serializer = JSONWebSignatureSerializer(secret)
    data = serializer.dumps(data)
    requests.post(url, data={'data': data})
