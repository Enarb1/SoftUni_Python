import os
from datetime import date, datetime
from multiprocessing import Value

import django
from django.db.models import Q, Count, F, Min, Avg, When
from sqlparse.sql import Case

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from main_app.models import House, Quest, Dragon
# Create queries within functions

def get_houses(search_string=None):


    if search_string is None or not search_string.strip():
        return "No houses match your search."

    query = Q(name__istartswith=search_string) | Q(motto__istartswith=search_string)
    houses = House.objects.filter(query).order_by('-wins', 'name')

    if not houses.exists():
        return "No houses match your search."

    result = []

    for h in houses:
        motto = h.motto if h.motto else "N/A"
        result.append(f"House: {h.name}, wins: {h.wins}, motto: {motto}")

    return "\n".join(result)

def get_most_dangerous_house():
    top_house = House.objects.get_houses_by_dragons_count().first()

    if not top_house or top_house.count_dragons == 0:
        return "No relevant data."

    ruling_status = "ruling" if top_house.is_ruling else "not ruling"
    return (f"The most dangerous house is the House of {top_house.name} with {top_house.count_dragons} dragons. "
            f"Currently {ruling_status} the kingdom.")

def get_most_powerful_dragon():
    top_dragon = Dragon.objects.filter(is_healthy=True).order_by('-power', 'name').first()

    if not top_dragon:
        return "No relevant data."


    return (f"The most powerful healthy dragon is {top_dragon.name} with a power level of {top_dragon.power:.1f}, "
            f"breath type {top_dragon.breath}, and {top_dragon.wins} wins, "
            f"coming from the house of {top_dragon.house.name}. "
            f"Currently participating in {top_dragon.dragon_quests.count()} quests.")

def update_dragons_data():
    injured_dragons = Dragon.objects.filter(is_healthy=False, power__gt=1.0)

    num_of_dragons_affected = injured_dragons.update(
        power=F('power') - 0.1,
        is_healthy=True
    )

    if num_of_dragons_affected == 0:
        return "No changes in dragons data."

    min_power = Dragon.objects.aggregate(min_power=Min('power'))['min_power']

    return (f"The data for {num_of_dragons_affected} dragon/s has been changed. "
            f"The minimum power level among all dragons is {min_power:.1f}")

def get_earliest_quest():
    quest = Quest.objects.order_by('start_time').first()

    if not quest:
        return "No relevant data."

    dragons = "*".join(quest.dragons.order_by('-power', 'name').values_list('name', flat=True))
    avg_power = quest.dragons.aggregate(avg_power=Avg('power'))['avg_power']

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
        return "No such quest."

    dragon = quest.dragons.order_by('-power', 'name').first()
    quest.dragons.filter(id=dragon.id).update(wins=F("wins") + 1)
    House.objects.filter(id=dragon.house.id).update(wins=F("wins") + 1)

    dragon.refresh_from_db()
    dragon.house.refresh_from_db()

    quest.delete()

    return (f"The quest: {quest.name} has been won by dragon {dragon.name} from house {dragon.house.name}. "
            f"The number of wins has been updated as follows: {dragon.wins} total wins for the dragon "
            f"and {dragon.house.wins} total wins for the house. The house was awarded with {quest.reward:.2f} coins.")
