from django.db import models


class SurfaceChoices(models.TextChoices):

    NOT_SELECTED = "Not Selected", "Not Selected"
    CLAY = "Clay", "Clay"
    GRASS = "Grass", "Grass"
    HARD_COURT = "Hard Court", "Hard Court"