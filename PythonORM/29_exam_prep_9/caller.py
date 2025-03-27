import os
from datetime import date

import django
from django.db.models import Q, Count, Sum, F, Avg

from main_app.choices import StatusChoices

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from main_app.models import Astronaut, Spacecraft, Mission


# Create queries within functions

def get_astronauts(search_string=None):
    query = Q(name__icontains=search_string) | Q(phone_number__icontains=search_string)

    if search_string is None or not Astronaut.objects.filter(query).exists():
        return ""

    astronauts = Astronaut.objects.filter(query).order_by("name")

    result = []

    for a in astronauts:
        status = "Active" if a.is_active else "Inactive"
        result.append(f"Astronaut: {a.name}, phone number: {a.phone_number}, status: {status}")

    return "\n".join(result)


def get_top_astronaut():
    top_astronaut = Astronaut.objects.get_astronauts_by_missions_count().first()

    if not top_astronaut or not Mission.objects.all().exists():
        return "No data."

    return f"Top Astronaut: {top_astronaut.name} with {top_astronaut.missions_count} missions."


def get_top_commander():
    top_commander = Astronaut.objects.annotate(
        commanded_missions_count=Count("commanded_missions")).order_by(
        "-commanded_missions_count","phone_number").first()

    if (not Astronaut.objects.all().exists()
            or not Mission.objects.all().exists()
            or Mission.objects.filter(commander__isnull=True).count() == Mission.objects.count()):
        return "No data."

    return f"Top Commander: {top_commander.name} with {top_commander.commanded_missions_count} commanded missions."


def get_last_completed_mission():
    mission = Mission.objects.filter(status=StatusChoices.COMPLETED).order_by("-launch_date").first()

    if not mission:
        return "No data."

    commander = mission.commander.name if mission.commander else "TBA"
    astronauts = ", ".join(mission.astronauts.order_by('name').values_list("name", flat=True))
    total_spacewalks = Mission.objects.filter(
        id=mission.id).aggregate(spacewalk_count=Sum("astronauts__spacewalks"))["spacewalk_count"]


    return (f"The last completed mission is: {mission.name}. "
            f"Commander: {commander}. "
            f"Astronauts: {astronauts}. "
            f"Spacecraft: {mission.spacecraft.name}. "
            f"Total spacewalks: {total_spacewalks}.")


def get_most_used_spacecraft():

    if not Mission.objects.all().exists():
        return "No data."

    spacecraft = Spacecraft.objects.annotate(
        mission_count=Count('missions')).order_by("-mission_count", 'name').first()

    astronauts_count = Astronaut.objects.filter(missions__spacecraft=spacecraft).distinct().count()

    return (f"The most used spacecraft is: {spacecraft.name}, "
            f"manufactured by {spacecraft.manufacturer}, "
            f"used in {spacecraft.mission_count} missions, "
            f"astronauts on missions: {astronauts_count}.")


def decrease_spacecrafts_weight():
    spacecraft_ids = Spacecraft.objects.filter(
        missions__status=StatusChoices.PLANNED, weight__gte=200.0).distinct().values_list("id", flat=True)

    updated_spacecraft = Spacecraft.objects.filter(id__in=spacecraft_ids).update(weight=F("weight") - 200.0)

    if updated_spacecraft == 0:
        return "No changes in weight."

    avg_weight = Spacecraft.objects.aggregate(avg_weight=Avg("weight"))["avg_weight"]

    return (f"The weight of {updated_spacecraft} spacecrafts has been decreased. "
            f"The new average weight of all spacecrafts is {avg_weight:.1f}kg")


