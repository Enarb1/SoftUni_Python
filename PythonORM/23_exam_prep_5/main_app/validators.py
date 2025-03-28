from django.contrib.messages.context_processors import messages
from django.core.exceptions import ValidationError


class RangeValidator:
    def __init__(self, min_value, max_value, message=None):
        self.min_value = min_value
        self.max_value = max_value
        self.message = message

    @property
    def message(self):
        return self.__message

    @message.setter
    def message(self, value):
        if value is None:
            value= f"Value must be between {self.min_value} and {self.max_value}"
        self.__message = value

    def __call__(self, value):
        if not self.min_value <= value <= self.max_value:
            raise ValidationError(self.message)

    def deconstruct(self):
        return (
            'main_app.validators.RangeValidator',
            [self.min_value, self.max_value],
            {'message': self.message},
        )
