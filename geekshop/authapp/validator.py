from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_name(value):
    if value.isdigit():
        raise ValidationError(
            _(f'Имя не может быть только цифрами'),
            params={'value': value},
        )

    if not value.isalpha():
        raise ValidationError(
            _(f'Имя пользователя не может содержать цифры'),
            params={'value': value}
        )

def validate_age(value):
    if value > 100:
        raise ValidationError(
            _(f'Возраст не может быть больше 100 лет'),
            params={'value': value}
        )