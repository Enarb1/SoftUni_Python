from django.core.exceptions import ValidationError


class OnlyLettersValidator:
    def __init__(self, message="Fruit name should contain only letters!"):
        self.message = message

    def __call__(self, value):
        if not value.isalpha():
            raise ValidationError(self.message)

    def deconstruct(self):
        return (
            'Frutipedia.frutipediaApp.validators.OnlyLettersValidator',
            (),
            {'message': self.message},
        )