from django.core.validators import MinLengthValidator, RegexValidator, MinValueValidator
from django.db import models

from main_app.choices import MissionStatus
from main_app.managers import AstronautManager


# Create your models here.

class NameUpdatedAt(models.Model):
    name = models.CharField(
        max_length=120,
        validators=[MinLengthValidator(2)],
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        abstract = True


class LaunchDate(models.Model):

    launch_date = models.DateField()

    class Meta:
        abstract = True


class Astronaut(NameUpdatedAt):
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
        default=0,
        validators=[MinValueValidator(0)],
    )

    objects = AstronautManager()

    def __str__(self):
        return self.name


class Spacecraft(NameUpdatedAt, LaunchDate):
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

class Mission(NameUpdatedAt, LaunchDate):
    description = models.TextField(
        blank=True,
        null=True,
    )

    status = models.CharField(
        max_length=9,
        choices=MissionStatus,
        default=MissionStatus.PLANNED
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
        null=True,
        related_name='commanded_missions',
    )

    def __str__(self):
        return self.name