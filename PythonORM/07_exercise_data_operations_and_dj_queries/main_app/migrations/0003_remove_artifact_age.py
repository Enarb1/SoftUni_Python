# Generated by Django 5.0.4 on 2025-02-13 21:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_artifact'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artifact',
            name='age',
        ),
    ]
