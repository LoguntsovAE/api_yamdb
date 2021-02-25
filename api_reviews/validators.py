import datetime as dt

from django.core.exceptions import ValidationError


def validate_year(value):
    if value > dt.datetime.today().year:
        raise ValidationError('Год не может быть больше текущего')
