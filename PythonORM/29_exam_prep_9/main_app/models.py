from django.core.validators import MinValueValidator, RegexValidator
from django.db import models

from main_app.choices import StatusChoices
from main_app.managers import AstronautManager
from main_app.mixins import NameMixin, UpdatedAtMixin, LaunchDateMixin


# Create your models here.

class Astronaut(NameMixin, UpdatedAtMixin):

    phone_number = models.CharField(
        max_length=15,
        validators=[RegexValidator(regex=r'^\d+$')],
        unique=True,
    )

    is_active = models.BooleanField(
        default=True,
    )

    date_of_birth = models.DateField(
        null=True,
        blank=True,
    )

    spacewalks = models.IntegerField(
        validators=[MinValueValidator(0)],
        default=0,
    )

    objects = AstronautManager()

    def __str__(self):
        return self.name


class Spacecraft(NameMixin, LaunchDateMixin ,UpdatedAtMixin):

    manufacturer = models.CharField(
        max_length=100,
    )

    capacity = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1)],
    )

    weight = models.FloatField(
        validators=[MinValueValidator(0.0)],
    )

    def __str__(self):
        return self.name


class Mission(NameMixin, LaunchDateMixin ,UpdatedAtMixin):

    description = models.TextField(
        null=True,
        blank=True,
    )

    status = models.CharField(
        max_length=9,
        choices=StatusChoices,
        default=StatusChoices.PLANNED
    )

    spacecraft = models.ForeignKey(
        to=Spacecraft,
        on_delete=models.CASCADE,
        related_name='missions',
    )

    astronauts = models.ManyToManyField(
        to=Astronaut,
        related_name='missions',
    )

    commander = models.ForeignKey(
        to=Astronaut,
        on_delete=models.SET_NULL,
        related_name='commanded_missions',
        null=True,
    )


    def __str__(self):
        return self.name


















