from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from main_app.managers import ProfileManager
from main_app.mixins import CreationDateMixin

# Create your models here.

class Profile(CreationDateMixin):

    full_name = models.CharField(
        max_length=100,
        validators=[MinLengthValidator(2)],
        help_text="User full name"
    )

    email = models.EmailField(
        help_text="User email",
    )

    phone_number = models.CharField(
        max_length=15,
        help_text="User phone number",
    )

    address = models.TextField(
        help_text="User address",
    )

    is_active = models.BooleanField(
        default=True
    )

    objects = ProfileManager()

    def __str__(self):
        return self.full_name


class Product(CreationDateMixin):

    name = models.CharField(
        max_length=100,
        help_text="Product name"
    )

    description = models.TextField()

    price = models.DecimalField(
        decimal_places=2,
        max_digits=10,
        validators=[MinValueValidator(0.01)],
        help_text="Product price"
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