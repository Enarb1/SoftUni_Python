from django.core.validators import MinLengthValidator, MinValueValidator, MaxValueValidator
from django.db import models

from main_app.managers import DirectorManager
from main_app.mixins import AwardedMixin, UpdatedMixin


# Create your models here.

class Base(models.Model):
    full_name = models.CharField(
        max_length=120,
        validators=[MinLengthValidator(2)]
    )

    birth_date = models.DateField(
        default='1900-01-01',
    )

    nationality = models.CharField(
        max_length=50,
        default='Unknown',
    )

    class Meta:
        abstract = True


class Director(Base):

    years_of_experience = models.SmallIntegerField(
        validators=[MinValueValidator(0)],
        default=0,
    )

    objects = DirectorManager()

class Actor(Base, AwardedMixin,UpdatedMixin):
    pass

class Movie(AwardedMixin, UpdatedMixin):
    class MovieGenreChoices(models.TextChoices):
        ACTION = 'Action', "Action"
        COMEDY = 'Comedy', "Comedy"
        DRAMA = 'Drama', "Drama"
        OTHER = 'Other', "Other"


    title = models.CharField(
        max_length=150,
        validators=[MinLengthValidator(5)]
    )

    release_date = models.DateField()

    storyline = models.TextField(
        blank=True,
        null=True,
    )

    genre = models.CharField(
        max_length=6,
        choices=MovieGenreChoices,
        default=MovieGenreChoices.OTHER
    )

    rating = models.DecimalField(
        decimal_places=1,
        max_digits=3,
        validators=[MinValueValidator(0.0), MaxValueValidator(10.0)],
        default=0.0
    )

    is_classic = models.BooleanField(
        default=False,
    )

    director = models.ForeignKey(
        Director,
        on_delete=models.CASCADE,
        related_name='director_movies',
    )
    starring_actor = models.ForeignKey(
        Actor,
        on_delete=models.SET_NULL,
        null=True,
        related_name='starring_movies',
    )

    actors = models.ManyToManyField(
        Actor,
        related_name='actor_movies'
    )