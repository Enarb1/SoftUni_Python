from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from main_app.managers import ProfileManager
from main_app.mixins import CreationDateMixin

# Create your models here.

class Profile(CreationDateMixin):

    full_name = models.CharField(
        max_length=100,
        validators=[MinLengthValidator(2)]
    )

    email = models.EmailField()

    phone_number = models.CharField(
        max_length=15,
    )

    address = models.TextField()

    is_active = models.BooleanField(
        default=True
    )

    objects = ProfileManager()

    def __str__(self):
        return self.full_name


class Product(CreationDateMixin):

    name = models.CharField(
        max_length=100,
    )

    description = models.TextField()

    price = models.DecimalField(
        decimal_places=2,
        max_digits=10,
        validators=[MinValueValidator(0.01)]
    )

    in_stock = models.PositiveIntegerField(
        validators=[MinValueValidator(0)]
    )

    is_available = models.BooleanField(
        default=True
    )

    def __str__(self):
        return self.name


class  Order(CreationDateMixin):

    profile = models.ForeignKey(
        to=Profile,
        on_delete=models.CASCADE,
        related_name='orders',
    )

    products = models.ManyToManyField(
        to=Product,
        related_name='orders',
    )

    total_price = models.DecimalField(
        decimal_places=2,
        max_digits=10,
        validators=[MinValueValidator(0.01)]
    )

    is_completed = models.BooleanField(
        default=False,
    )


    def __str__(self):
        return self.profile.full_name