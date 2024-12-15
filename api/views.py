from django.http import JsonResponse
from django.http import HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
import json

from robots.models import Robot
from .validators import validate_body


@csrf_exempt
def index(request):
    if request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        try:
            body = json.loads(body_unicode)
        except ValueError as e:
            raise HttpResponseBadRequest(e)
        validate_body(body)
        body['serial'] = f'{body["model"]}-{body["version"]}'
        robot = Robot(**body)
        robot.save()
        data = {
            'result': 'OK',
            'robot': {
                'id': robot.id,
                'serial': robot.serial,
                'model': robot.model,
                'version': robot.version,
                'created': robot.created,
            },
        }
        return JsonResponse(data)
    else:
        return HttpResponseBadRequest('Only POST method here.')
