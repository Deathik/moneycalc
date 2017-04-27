from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _


def more_than_zero_validator(value):
    if value <= 0:
        raise ValidationError(
            _('%(value)s is less or equal to zero'), params={'value': value},
        )
