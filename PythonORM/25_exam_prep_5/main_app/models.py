from django.core.validators import MinLengthValidator
from django.db import models

from main_app.managers import AuthorManager
from main_app.validators import NumberRangeValidator
from main_app.choices import CategoryChoices

# Create your models here.

class PublishedBaseField(models.Model):

    published_on = models.DateTimeField(
        auto_now_add=True,
        editable=False,
    )

    class Meta:
        abstract = True


class ContentBaseField(models.Model):

    content = models.TextField(
        validators=[MinLengthValidator(10)],
    )

    class Meta:
        abstract = True


class Author(models.Model):

    full_name = models.CharField(
        max_length=100,
        validators=[MinLengthValidator(3)],
    )

    email = models.EmailField(
        unique=True,
    )

    is_banned = models.BooleanField(
        default=False,
    )

    birth_year = models.PositiveIntegerField(
        validators=[NumberRangeValidator(1900, 2005)],
    )

    website = models.URLField(
        blank=True,
        null=True,
    )
    objects = AuthorManager()

    def __str__(self):
        return self.full_name

class Article(ContentBaseField, PublishedBaseField):

    title = models.CharField(
        max_length=200,
        validators=[MinLengthValidator(5)],
    )

    category = models.CharField(
        max_length=10,
        choices=CategoryChoices,
        default=CategoryChoices.TECHNOLOGY,
    )

    authors = models.ManyToManyField(
        Author,
        related_name='articles',
    )

    def __str__(self):
        return self.title


class Review(ContentBaseField, PublishedBaseField):

    rating = models.FloatField(
        validators=[NumberRangeValidator(1.0, 5.0)],
    )

    author = models.ForeignKey(
        to=Author,
        on_delete=models.CASCADE,
        related_name='reviews',
    )

    article = models.ForeignKey(
        to=Article,
        on_delete=models.CASCADE,
        related_name='reviews',
    )


    def __str__(self):
        return self.article.title