# Generated by Django 5.0.4 on 2025-02-28 15:59

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_restaurantreview'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurantreview',
            name='rating',
            field=models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(5)]),
        ),
    ]
