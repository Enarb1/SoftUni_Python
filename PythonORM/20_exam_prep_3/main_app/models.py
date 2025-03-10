from django.core.validators import MinLengthValidator, MinValueValidator, MaxValueValidator, RegexValidator
from django.db import models

from datetime import date

from main_app.managers import HouseManager


# Create your models here.


class BaseData(models.Model):
    name = models.CharField(
        max_length=80,
        validators=[MinLengthValidator(5)],
        unique=True,
    )

    modified_at = models.DateTimeField(
        auto_now=True,
    )

    wins = models.PositiveSmallIntegerField(
        default=0,
    )

    class Meta:
        abstract = True


class House(BaseData):
    motto = models.TextField(
        blank=True,
        null=True,
    )

    is_ruling = models.BooleanField(
        default=False,
    )

    castle = models.CharField(
        max_length=80,
        blank=True,
        null=True,
    )

    objects = HouseManager()

    def __str__(self):
        return self.name

class Dragon(BaseData):
    class BreathChoices(models.TextChoices):
        FIRE = "Fire", "Fire"
        ICE = "Ice", "Ice"
        LIGHTNING = "Lightning", "Lightning"
        UNKNOWN = "Unknown", "Unknown"

    power = models.DecimalField(
        decimal_places=1,
        max_digits=3,
        validators=[MinValueValidator(1.0), MaxValueValidator(10.0)],
        default=1.0,
    )

    breath = models.CharField(
        max_length=9,
        choices=BreathChoices,
        default=BreathChoices.UNKNOWN,
    )

    is_healthy = models.BooleanField(
        default=True,
    )

    birth_date = models.DateField(
        default=date.today,
    )

    house = models.ForeignKey(
        to=House,
        on_delete=models.CASCADE,
        related_name='dragons',
    )

    def __str__(self):
        return self.name

class Quest(models.Model):
    name = models.CharField(
        max_length=80,
        validators=[MinLengthValidator(5)],
        unique=True,
    )

    code = models.CharField(
        max_length=4,
        validators=[RegexValidator(regex=r'^[A-Za-z#]{4}$')],
        unique=True,
    )

    reward = models.FloatField(
        default=100,
    )

    start_time = models.DateTimeField()

    modified_at = models.DateTimeField(
        auto_now=True,
    )

    dragons = models.ManyToManyField(
        to=Dragon,
        related_name='dragon_quests',
    )

    host = models.ForeignKey(
        to=House,
        on_delete=models.CASCADE,
        related_name='hosted_quests',
    )

    def __str__(self):
        return self.name

