from django.core.validators import MinValueValidator, MinLengthValidator
from django.db import models

from Frutipedia.fruitipediaApp.validators import OnlyLettersValidator


class Category(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True,
    )

    def __str__(self):
        return self.name


class Fruit(models.Model):
    name = models.CharField(
        max_length=30,
        validators=[
            MinLengthValidator(2),
            OnlyLettersValidator()
        ],
    )

    image_url = models.URLField()

    description = models.TextField()

    nutrition = models.IntegerField(
        blank=True,
        null=True,
    )

    category = models.ForeignKey(
        to=Category,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.name
