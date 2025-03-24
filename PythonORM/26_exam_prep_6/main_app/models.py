from datetime import date

from django.core.validators import MinLengthValidator, RegexValidator
from django.db import models

from main_app.choices import BreathChoices
from main_app.managers import HouseManager
from main_app.validators import RangeValidator


# Create your models here.


class NameBaseField(models.Model):

    name = models.CharField(
        max_length=80,
        validators=[MinLengthValidator(5)],
        unique=True,
    )

    class Meta:
        abstract = True


class WinsBaseField(models.Model):

    wins = models.PositiveSmallIntegerField(
        default=0,
    )

    class Meta:
        abstract = True


class ModifiedAtBaseField(models.Model):

    modified_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        abstract = True


class House(NameBaseField, ModifiedAtBaseField, WinsBaseField):

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


class Dragon(NameBaseField, ModifiedAtBaseField, WinsBaseField):

    power = models.DecimalField(
        decimal_places=1,
        max_digits=3,
        validators=[RangeValidator(1.0, 10.0)],
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


class Quest(NameBaseField, ModifiedAtBaseField):

    code = models.CharField(
        max_length=4,
        validators=[RegexValidator(regex=r'^[A-Za-z#]{4}$')],
        unique=True,
    )

    reward = models.FloatField(
        default=100.0,
    )

    start_time = models.DateTimeField()

    dragons = models.ManyToManyField(
        to=Dragon,
        related_name='quests',
    )

    host = models.ForeignKey(
        to=House,
        on_delete=models.CASCADE,
        related_name='quests_hosted',
    )

    def __str__(self):
        return self.name
