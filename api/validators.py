import datetime

from django.core.exceptions import BadRequest


def validate_body(body):
    """Количество полей и в цикле каждое длина и символы, датавремя."""
    if len(body) != 3:
        raise BadRequest('More JSON data, please.')
    for key in body:
        validate_len(key, body)
        validate_symbol(key, body)
    validate_datetime('created', body)


def validate_len(key, body):
    if key in ['model', 'version']:
        if len(body[key]) != 2:
            raise BadRequest(f'Check length in "{key}" data, please.')
        elif key == 'created':
            if len(body[key]) != 19:
                raise BadRequest(f'Check length in "{key}" data, please.')
        else:
            pass


def validate_symbol(key, body):
    if key in ['model', 'version']:
        if not body[key].isalnum():
            raise BadRequest(f'Check symbol in "{key}" data, please.')


def validate_datetime(key, body):
    try:
        datetime.datetime.strptime(body[key], '%Y-%m-%d %H:%M:%S')
    except Exception as e:
        raise BadRequest(f'Check format in "{key}" data, please.{e}')
