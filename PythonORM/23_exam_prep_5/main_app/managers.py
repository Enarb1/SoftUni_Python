from django.db import models
from django.db.models import Count


class TennisManager(models.Manager):
   def get_tennis_players_by_wins_count(self):
       return self.annotate(win_counts=Count('won_matches')).order_by('-win_counts', 'full_name')