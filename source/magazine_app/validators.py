from django.utils.deconstruct import deconstructible

from django.core.validators import BaseValidator


@deconstructible
class MinValueValidator(BaseValidator):
    message = 'Значение не может быть меньше %(limit_value)s.'
    code = 'min_value'

    def compare(self, a, b):
        return a < b
