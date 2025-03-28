from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from main_app.choices import GenreChoices
from main_app.managers import DirectorManager
from main_app.validators import RangeValidator


# Create your models here.


class BasePerson(models.Model):

    full_name = models.CharField(
        max_length=120,
        validators=[MinLengthValidator(2)],
    )

    birth_date = models.DateField(
        default='1900-01-01'
    )

    nationality = models.CharField(
        max_length=50,
        default='Unknown',
    )

    class Meta:
        abstract = True


class IsAwardedField(models.Model):

    is_awarded = models.BooleanField(
        default=False,
    )

    class Meta:
        abstract = True


class LastUpdatedField(models.Model):

    last_updated = models.DateTimeField(
        auto_now=True,
    )

    class Meta:
        abstract = True


class Director(BasePerson):

    objects = DirectorManager()

    years_of_experience = models.SmallIntegerField(
        validators=[MinValueValidator(0)],
        default=0,
    )

    def __str__(self):
        return self.full_name


class Actor(BasePerson, IsAwardedField, LastUpdatedField):

    def __str__(self):
        return self.full_name


class Movie(IsAwardedField, LastUpdatedField):

    title = models.CharField(
        max_length=150,
        validators=[MinLengthValidator(5)],
    )

    release_date = models.DateField()

    storyline = models.TextField(
        blank=True,
        null=True,
    )

    genre = models.CharField(
        max_length=6,
        choices=GenreChoices,
        default=GenreChoices.OTHER,
    )

    rating = models.DecimalField(
        max_digits=3,
        decimal_places=1,
        validators=[RangeValidator(0.0, 10.0)],
        default=0.0,
    )

    is_classic  = models.BooleanField(
        default=False,
    )

    director = models.ForeignKey(
        to=Director,
        on_delete=models.CASCADE,
        related_name='director_movies',
    )

    starring_actor = models.ForeignKey(
        to=Actor,
        on_delete=models.SET_NULL,
        null=True,
        related_name='starring_movies',
    )

    actors = models.ManyToManyField(
        to=Actor,
        related_name='actor_movies',
    )

    def __str__(self):
        return self.title