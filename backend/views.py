from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from backend.utils import endpoint


@require_POST
@csrf_exempt
def push(request, target):
    return endpoint.push(request, target)


def index(request):
    return HttpResponse('hi')
