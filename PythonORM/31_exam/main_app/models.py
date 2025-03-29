from django.core.validators import MinLengthValidator
from django.db import models

from main_app.choices import GenreChoices
from main_app.managers import PublisherManager
from main_app.mixins import NameMixin, CountryMixin, RatingMixin, UpdatedAtMixin
from main_app.validators import RangeValidator


# Create your models here.


class Publisher(NameMixin, CountryMixin, RatingMixin):

    established_date = models.DateField(
        default='1800-01-01',
    )

    objects = PublisherManager()

    def __str__(self):
        return self.name


class Author(NameMixin, CountryMixin, UpdatedAtMixin):

    birth_date = models.DateField(
        blank=True,
        null=True,
    )

    is_active = models.BooleanField(
        default=True,
    )

    def __str__(self):
        return self.name


class Book(RatingMixin, UpdatedAtMixin):

    title = models.CharField(
        max_length=200,
        validators=[MinLengthValidator(2)],
    )

    publication_date = models.DateField()

    summary = models.TextField(
        blank=True,
        null=True,
    )

    genre = models.CharField(
        max_length=11,
        choices=GenreChoices,
        default=GenreChoices.OTHER,
    )

    price = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        validators=[RangeValidator(0.01, 9999.99)],
        default=0.01,
    )

    is_bestseller = models.BooleanField(
        default=False,
    )

    publisher = models.ForeignKey(
        to=Publisher,
        on_delete=models.CASCADE,
        related_name='books',
    )

    main_author = models.ForeignKey(
        to=Author,
        on_delete=models.CASCADE,
        related_name='books',
    )

    co_authors = models.ManyToManyField(
        to=Author,
        related_name='coauthored_books',
    )

    def __str__(self):
        return self.title
