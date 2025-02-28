from django.db import models


class ManagerChoices(models.TextChoices):
    TEAM_LEADER = "Team Leader", "Team Leader"
    TECH_TEAM_LEAD = "Tech Team Lead", "Tech Team Lead"
    CEO = "CEO", "CEO"

class AgentTypeChoices(models.TextChoices):
    LEVEL_1 = "Level 1", "Level 1"
    LEVEL_2 = "Level 2", "Level 2"
    LEVEL_3 = "Level 3", "Level 3"

