import os
from decimal import Decimal

import django
from django.db.models import Q, Min, Avg

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from main_app.models import House, Dragon, Quest
# Create queries within functions

def get_houses(search_string=None):


    if not search_string or not search_string.strip():
        return "No houses match your search."

    query = Q(name__istartswith=search_string) | Q(motto__istartswith=search_string)

    houses = House.objects.filter(query).order_by("-wins", "name")

    if not houses.exists():
        return "No houses match your search."

    result = []

    for h in houses:
        motto = h.motto or 'N/A'
        result.append(f"House: {h.name}, wins: {h.wins}, motto: {motto}")

    return "\n".join(result)


def get_most_dangerous_house():
    house = House.objects.get_houses_by_dragons_count().first()

    if not house or not Dragon.objects.exists():
        return "No relevant data."

    is_ruling = "ruling" if house.is_ruling else "not ruling"

    return (f"The most dangerous house is the House of {house.name} "
            f"with {house.dragons.count()} dragons. Currently {is_ruling} the kingdom.")


def get_most_powerful_dragon():
    dragon = Dragon.objects.filter(is_healthy=True).order_by("-power", "name").first()

    if not dragon:
        return "No relevant data."

    return (f"The most powerful healthy dragon is {dragon.name} "
            f"with a power level of {dragon.power:.1f}, breath type {dragon.breath}, "
            f"and {dragon.wins} wins, coming from the house of {dragon.house.name}. "
            f"Currently participating in {dragon.quests.count()} quests.")


def update_dragons_data():
    dragons = Dragon.objects.filter(is_healthy=False, power__gt=1.0)

    updated_dragons = 0

    for d in dragons:
        d.power = max(d.power - Decimal(0.1), Decimal(1.0))
        d.is_healthy = True
        updated_dragons += 1
        d.save()

    if updated_dragons == 0:
        return "No changes in dragons data."

    min_power = Dragon.objects.aggregate(min_power=Min("power"))["min_power"]

    return (f"The data for {updated_dragons} dragon/s has been changed. "
            f"The minimum power level among all dragons is {min_power:.1f}")


def get_earliest_quest():
    quest  = Quest.objects.all().order_by("start_time").first()

    if not quest:
        return "No relevant data."

    dragons = "*".join(quest.dragons.order_by("-power", "name").values_list("name", flat=True))
    avg_power = quest.dragons.aggregate(avg_power=Avg("power"))["avg_power"]

    return (f"The earliest quest is: {quest.name}, "
            f"code: {quest.code}, "
            f"start date: {quest.start_time.day}.{quest.start_time.month}.{quest.start_time.year}, "
            f"host: {quest.host.name}. "
            f"Dragons: {dragons}. "
            f"Average dragons power level: {avg_power:.2f}")


def announce_quest_winner(quest_code):
    try:
        quest = Quest.objects.get(code=quest_code)
    except Quest.DoesNotExist:
        return  "No such quest."

    top_dragon = quest.dragons.order_by("-power", "name").first()
    top_dragon.wins += 1
    top_dragon.house.wins += 1
    top_dragon.save()
    top_dragon.house.save()

    quest.delete()

    return (f"The quest: {quest.name} has been won by dragon {top_dragon.name} from house {top_dragon.house.name}. "
            f"The number of wins has been updated as follows: {top_dragon.wins} total wins for the dragon "
            f"and {top_dragon.house.wins} total wins for the house. "
            f"The house was awarded with {quest.reward:.2f} coins.")
