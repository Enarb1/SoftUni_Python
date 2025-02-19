import os
from typing import List

import django

from main_app.choices import OperationSystemChoices, MealTypeChoices, DifficultyChoices, WorkoutTypeChoices

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models
from main_app.models import ArtworkGallery, Laptop, ChessPlayer, Meal, Dungeon, Workout
from django.db.models import Case, When, Value
# Create and check models

def show_highest_rated_art():
    artwork = ArtworkGallery.objects.all().order_by('-rating', 'id').first()
    return f"{artwork.art_name} is the highest-rated art with a {artwork.rating} rating!"

def bulk_create_arts(first_art: ArtworkGallery, second_art: ArtworkGallery):
    ArtworkGallery.objects.bulk_create([
        first_art,
        second_art
    ])

def delete_negative_rated_arts():
    ArtworkGallery.objects.filter(rating__lt=0).delete()

def show_the_most_expensive_laptop():
    laptop = Laptop.objects.order_by('-price', '-id').first()

    return f"{laptop.brand} is the most expensive laptop available for {laptop.price}$!"

def bulk_create_laptops(args: List[Laptop]):
    Laptop.objects.bulk_create(args)

def update_to_512_GB_storage():
    Laptop.objects.filter(brand__in=("Asus", "Lenovo")).update(storage=512)

def update_to_16_GB_memory():
    Laptop.objects.filter(brand__in=("Apple", "Dell", "Acer")).update(memory=16)

def update_operation_systems():
    Laptop.objects.update(
        operation_system=Case(
            When(brand="Asus", then=Value(OperationSystemChoices.WINDOWS)),
            When(brand="Apple", then=Value(OperationSystemChoices.MACOS)),
            When(brand__in=("Dell", "Acer"), then=Value(OperationSystemChoices.LINUX)),
            When(brand="Lenovo", then=Value(OperationSystemChoices.CHROME_OS))
        )
    )

def delete_inexpensive_laptops():
    Laptop.objects.filter(price__lt=1200).delete()

def bulk_create_chess_players(args: List[ChessPlayer]):
    ChessPlayer.objects.bulk_create(args)

def delete_chess_players():
    ChessPlayer.objects.filter(title="no title").delete()

def change_chess_games_won():
    ChessPlayer.objects.filter(title="GM").update(games_won=30)

def change_chess_games_lost():
    ChessPlayer.objects.filter(title="no title").update(games_lost=25)

def change_chess_games_drawn():
    ChessPlayer.objects.update(games_drawn=10)

def grand_chess_title_GM():
    ChessPlayer.objects.filter(rating__gte=2400).update(title="GM")

def grand_chess_title_IM():
    ChessPlayer.objects.filter(rating__range=[2300, 2399]).update(title="IM")

def grand_chess_title_FM():
    ChessPlayer.objects.filter(rating__range=[2200, 2299]).update(title="FM")

def grand_chess_title_regular_player():
    ChessPlayer.objects.filter(rating__range=[0, 2199]).update(title="regular player")

def set_new_chefs():
    Meal.objects.filter(meal_type=MealTypeChoices.BREAKFAST).update(chef="Gordon Ramsay")
    Meal.objects.filter(meal_type=MealTypeChoices.LUNCH).update(chef="Julia Child")
    Meal.objects.filter(meal_type=MealTypeChoices.DINNER).update(chef="Jamie Oliver")
    Meal.objects.filter(meal_type=MealTypeChoices.SNACK).update(chef="Thomas Keller")

def set_new_preparation_times():
    Meal.objects.update(
        preparation_time=Case(
            When(meal_type=MealTypeChoices.BREAKFAST,then=Value("10 minutes")),
            When(meal_type=MealTypeChoices.LUNCH, then=Value("12 minutes")),
            When(meal_type=MealTypeChoices.DINNER, then=Value("15 minutes")),
            When(meal_type=MealTypeChoices.SNACK, then=Value("5 minutes")),
        )
    )

def update_low_calorie_meals():
    Meal.objects.filter(
        meal_type__in=(
            MealTypeChoices.BREAKFAST,
            MealTypeChoices.DINNER
        )
    ).update(calories=400)

def update_high_calorie_meals():
    Meal.objects.filter(
        meal_type__in=(
            MealTypeChoices.LUNCH,
            MealTypeChoices.SNACK
        )
    ).update(calories=700)

def delete_lunch_and_snack_meals():
    Meal.objects.filter(
        meal_type__in=(
            MealTypeChoices.LUNCH,
            MealTypeChoices.SNACK
        )
    ).delete()

def show_hard_dungeons():
    result = []
    hard_dungeons = Dungeon.objects.filter(difficulty=DifficultyChoices.HARD).order_by('-location')

    for hd in hard_dungeons:
        result.append(f"{hd.name} is guarded by {hd.boss_name} who has {hd.boss_health} health points!")

    return "\n".join(result)

def bulk_create_dungeons(args: List[Dungeon]):
    Dungeon.objects.bulk_create(args)

def update_dungeon_names():
    Dungeon.objects.update(
        name=Case(
            When(difficulty=DifficultyChoices.EASY, then=Value("The Erased Thombs")),
            When(difficulty=DifficultyChoices.MEDIUM, then=Value("The Coral Labyrinth")),
            When(difficulty=DifficultyChoices.HARD, then=Value("The Lost Haunt")),
        )
    )

def update_dungeon_bosses_health():
    Dungeon.objects.exclude(
        difficulty=DifficultyChoices.EASY,
    ).update(boss_health=500)

def update_dungeon_recommended_levels():
    Dungeon.objects.update(
        recommended_level=Case(
            When(difficulty=DifficultyChoices.EASY, then=Value(25)),
            When(difficulty=DifficultyChoices.MEDIUM, then=Value(50)),
            When(difficulty=DifficultyChoices.HARD, then=Value(75)),
        )
    )

def update_dungeon_rewards():
    Dungeon.objects.update(
        reward=Case(
            When(boss_health=500,then=Value("1000 Gold")),
            When(location__startswith="E", then=Value("New dungeon unlocked")),
            When(location__endswith="s", then=Value("Dragonheart Amulet")),
        )
    )

def set_new_locations():
    Dungeon.objects.update(
        location=Case(
            When(recommended_level=25, then=Value("Enchanted Maze")),
            When(recommended_level=50, then=Value("Grimstone Mines")),
            When(recommended_level=75, then=Value("Shadowed Abyss")),
        )
    )

def show_workouts():
   workouts = Workout.objects.filter(
        workout_type__in=(
            WorkoutTypeChoices.CALISTHENICS,
            WorkoutTypeChoices.CROSSFIT
        )
    ).order_by('id')

   return "\n".join(str(w) for w in workouts)

def get_high_difficulty_cardio_workouts():
    return Workout.objects.filter(
        workout_type=WorkoutTypeChoices.CARDIO,
        difficulty="High"
    ).order_by('instructor')

def set_new_instructors():
    Workout.objects.update(
        instructor=Case(
            When(workout_type=WorkoutTypeChoices.CARDIO, then=Value("John Smith")),
            When(workout_type=WorkoutTypeChoices.STRENGTH, then=Value("Michael Williams")),
            When(workout_type=WorkoutTypeChoices.YOGA, then=Value("Emily Johnson")),
            When(workout_type=WorkoutTypeChoices.CROSSFIT, then=Value("Sarah Davis")),
            When(workout_type=WorkoutTypeChoices.CALISTHENICS, then=Value("Chris Heria"))
        )
    )

def set_new_duration_times():
    Workout.objects.update(
        duration=Case(
            When(instructor="John Smith", then=Value("15 minutes")),
            When(instructor="Sarah Davis", then=Value("30 minutes")),
            When(instructor="Chris Heria", then=Value("45 minutes")),
            When(instructor="Michael Williams", then=Value("1 hour")),
            When(instructor="Emily Johnson", then=Value("1 hour and 30 minutes")),
        )
    )

def delete_workouts():
    Workout.objects.exclude(
        workout_type__in=(
            WorkoutTypeChoices.CALISTHENICS,
            WorkoutTypeChoices.STRENGTH
        )
    ).delete()

# Run and print your queries
