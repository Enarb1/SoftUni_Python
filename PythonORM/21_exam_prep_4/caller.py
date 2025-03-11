import os
from datetime import date
from multiprocessing import Value
from pydoc_data.topics import topics

import django
from django.db.models import Q, Count, Sum, Avg, F, When
from django.forms import DecimalField
from sqlparse.sql import Case

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from main_app.choices import MissionStatus
from main_app.models import Mission, Spacecraft, Astronaut
# Create queries within functions

def populate_db():

    astronauts = [
        Astronaut(
            name="John Deer",
            phone_number="853967",
            is_active=True,
            date_of_birth=date(1980, 1, 1),
            spacewalks=3,
        ),
        Astronaut(
            name="Jane Smith",
            phone_number="123456",
            is_active=True,
            date_of_birth=date(1985, 5, 15),
            spacewalks=1,
        ),
        Astronaut(
            name="Josie Stam",
            phone_number="111111",
            is_active=False,
            date_of_birth=date(1990, 3, 12),
            spacewalks=0,
        )
    ]
    Astronaut.objects.bulk_create(astronauts)

    john = Astronaut.objects.get(name="John Deer")
    jane = Astronaut.objects.get(name="Jane Smith")
    josie = Astronaut.objects.get(name="Josie Stam")

    spacecrafts = [
        Spacecraft(
            name="Explorer I",
            manufacturer="SpaceTech Inc.",
            capacity=5,
            launch_date=date(2022, 1, 1),
            weight=12000.5,
        ),
        Spacecraft(
            name="Explorer II",
            manufacturer="SpaceX",
            capacity=2,
            launch_date=date(2023, 5, 1),
            weight=10000.2,
        )
    ]
    Spacecraft.objects.bulk_create(spacecrafts)

    explorer_1 = Spacecraft.objects.get(name="Explorer I")

    missions = [
        Mission(
            name="Moon Landing",
            description="Landing on the moon",
            status=MissionStatus.PLANNED,
            launch_date=date(2024, 10, 10),
            spacecraft=explorer_1,
            commander=john,
        ),
        Mission(
            name="Moon Landing2",
            description="Landing on the moon",
            status=MissionStatus.COMPLETED,
            launch_date=date(2024, 3, 1),
            spacecraft=explorer_1,
            commander=josie,
        )
    ]
    Mission.objects.bulk_create(missions)

    moon_landing = Mission.objects.get(name="Moon Landing")
    moon_landing_2 = Mission.objects.get(name="Moon Landing2")

    moon_landing.astronauts.add(john, jane)
    moon_landing_2.astronauts.add(jane, josie)

    print('DB populated')


def get_astronauts(search_string=None):
    if search_string is None:
        return ""

    query = Q(name__icontains=search_string) | Q(phone_number__icontains=search_string)
    astronauts = Astronaut.objects.filter(query).order_by("name")

    if not astronauts.exists():
        return ""

    result = []

    for a in astronauts:
        result.append(
            f"Astronaut: {a.name}, "
            f"phone number: {a.phone_number}, "
            f"status: {'Active' if a.is_active else 'Inactive'}"
        )

    return "\n".join(result)

def get_top_astronaut():
    top_astronaut = Astronaut.objects.get_astronauts_by_missions_count().first()

    if not top_astronaut or not Mission.objects.all().exists():
        return "No data."

    return f"Top Astronaut: {top_astronaut.name} with {top_astronaut.missions_count} missions."

def get_top_commander():
    top_commander = Astronaut.objects.annotate(
        missions_count=Count("commanded_missions")
    ).order_by("-missions_count", "phone_number").first()

    if not top_commander or top_commander.missions_count == 0:
        return "No data."

    return f"Top Commander: {top_commander.name} with {top_commander.missions_count} commanded missions."

def get_last_completed_mission():
    lcm = Mission.objects.filter(status=MissionStatus.COMPLETED).order_by("-launch_date").first()

    if lcm is None:
        return "No data."

    commander_name = lcm.commander.name if lcm.commander else "TBA"
    astronauts = ", ".join(lcm.astronauts.order_by("name").values_list("name", flat=True))
    spacewalks_total = lcm.astronauts.aggregate(total_spacewalks=Sum('spacewalks'))['total_spacewalks']

    return (f"The last completed mission is: {lcm.name}. "
            f"Commander: {commander_name}. "
            f"Astronauts: {astronauts}. "
            f"Spacecraft: {lcm.spacecraft.name}. "
            f"Total spacewalks: {spacewalks_total}.")

def get_most_used_spacecraft():

    if not Mission.objects.all().exists():
        return "No data."

    spacecraft = Spacecraft.objects.prefetch_related("missions").annotate(
        missions_count=Count("missions")
    ).order_by("-missions_count").first()

    mission_astronauts_count = spacecraft.missions.aggregate(
        total_astronauts=Count("astronauts", distinct=True)
    )['total_astronauts']

    return (f"The most used spacecraft is: {spacecraft.name}, "
            f"manufactured by {spacecraft.manufacturer}, used in {spacecraft.missions_count} missions, "
            f"astronauts on missions: {mission_astronauts_count}.")

def decrease_spacecrafts_weight():
    spacecrafts = Spacecraft.objects.filter(
        missions__status=MissionStatus.PLANNED, weight__gte=200.00).distinct()

    updated_spacecrafts = 0

    for s in spacecrafts:
        new_weight = max(s.weight - 200, 0.0)
        s.weight = new_weight
        s.save()
        updated_spacecrafts += 1

    if updated_spacecrafts == 0:
        return "No changes in weight."

    avg_weight = Spacecraft.objects.aggregate(avg_weight=Avg('weight'))['avg_weight']

    return (f"The weight of {updated_spacecrafts} spacecrafts has been decreased. "
            f"The new average weight of all spacecrafts is {avg_weight:.1f}kg")
