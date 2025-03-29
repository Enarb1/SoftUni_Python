from django.core.validators import MinLengthValidator, MinValueValidator, MaxValueValidator
from django.db import models

from main_app.validators import RangeValidator


class NameMixin(models.Model):
    name = models.CharField(
        max_length=100,
        validators=[MinLengthValidator(3)],
    )

    class Meta:
        abstract = True


class CountryMixin(models.Model):
    country = models.CharField(
        max_length=40,
        default="TBC",
    )

    class Meta:
        abstract = True


class RatingMixin(models.Model):
    rating = models.FloatField(
        validators=[RangeValidator(0.0, 5.0)],
        default=0.0,
    )

    class Meta:
        abstract = True


class UpdatedAtMixin(models.Model):
    updated_at = models.DateTimeField(
        auto_now=True,
    )

    class Meta:
        abstract = True