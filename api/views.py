import json
from datetime import datetime

from django.http import HttpResponseBadRequest, JsonResponse
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt

from robots.models import Robot

from .validators import validate_body


@csrf_exempt
def index(request):
    """Эндпоинт добавления робота."""
    if request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        try:
            body = json.loads(body_unicode)
        except ValueError as e:
            raise HttpResponseBadRequest(e)
        validate_body(body)
        body['created'] = timezone.make_aware(
            datetime.strptime(f'{body["created"]}', "%Y-%m-%d %H:%M:%S")
        )
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
