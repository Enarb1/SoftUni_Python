from django.db import models
from django.db.models import Count


class HouseManager(models.Manager):
    def get_houses_by_dragons_count(self):
        return self.annotate(
            count_dragons=Count('dragons')
        ).order_by('-count_dragons', 'name')