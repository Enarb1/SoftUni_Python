import os
import django
from django.db.models import F

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from main_app.models import Pet, Artifact, Location, Car, Task, HotelRoom, Character


# Create queries within functions

def create_pet(name: str, species: str):
    pet = Pet.objects.create(
        name=name,
        species=species
    )

    return f"{pet.name} is a very cute {pet.species}!"

def create_artifact(name: str, origin: str, age: int, description: str, is_magical: bool):
    artifact = Artifact.objects.create(
        name=name,
        origin=origin,
        age=age,
        description=description,
        is_magical=is_magical,
    )

    return f"The artifact {artifact.name} is {artifact.age} years old!"

def rename_artifact(artifact: Artifact, new_name: str):

    if artifact.is_magical  and artifact.age > 250:
        artifact.name = new_name
        artifact.save()

def delete_all_artifacts():
    Artifact.objects.all().delete()

def show_all_locations():
    locations = Location.objects.all().order_by("-id")

    return "\n".join(str(l) for l in locations)

def new_capital():
    location = Location.objects.first()
    location.is_capital = True
    location.save()

def get_capitals():
    return  Location.objects.filter(is_capital=True).values("name")

def delete_first_location():
    Location.objects.first().delete()

def apply_discount():
    cars = Car.objects.all()

    for car in cars:
        percentage = sum(int(d) for d in str(car.year)) / 100
        discount = float(car.price ) * percentage
        car.price_with_discount = float(car.price) - discount

    Car.objects.bulk_update(cars,["price_with_discount"])

def get_recent_cars():
    return Car.objects.all().filter(year__gt=2020).values("model", "price")

def delete_last_car():
    Car.objects.last().delete()

def show_unfinished_tasks():
    tasks = Task.objects.all().filter(is_finished=False)

    return "\n".join(str(t) for t in tasks)

def complete_odd_tasks():
    tasks = Task.objects.all().filter(is_finished=False)

    for task in tasks:
        if task.id % 2 != 0:
            task.is_finished = True

    Task.objects.bulk_update(tasks,["is_finished"])

def encode_and_replace(text: str, task_title: str):
    decoded_text = "".join(chr(ord(t) - 3) for t in text)
    Task.objects.all().filter(title=task_title).update(description=decoded_text)

def get_deluxe_rooms():
    rooms = HotelRoom.objects.all().filter(room_type="Deluxe")

    return "\n".join(str(r) for r in rooms if r.id % 2 == 0)

def increase_room_capacity():
    hotel_rooms = HotelRoom.objects.all()
    previous_room_capacity = None
    for room in hotel_rooms:
        if not room.is_reserved:
            continue
        if previous_room_capacity is not None:
            room.capacity += previous_room_capacity
        else:
            room.capacity += room.id

        previous_room_capacity = room.capacity

    HotelRoom.objects.bulk_update(hotel_rooms,["capacity"])

def reserve_first_room():
    room = HotelRoom.objects.first()
    room.is_reserved = True
    room.save()

def delete_last_room():
    room = HotelRoom.objects.last()
    if not room.is_reserved:
        room.delete()


def update_characters():
    Character.objects.filter(class_name="Mage").update(
        level=F("level") + 3,
        intelligence=F("intelligence") - 7,
    )

    Character.objects.filter(class_name="Warrior").update(
        hit_points=F("hit_points") / 2,
        dexterity=F("dexterity") + 4,
    )

    Character.objects.filter(class_name__in=["Assassin", "Scout"]).update(
        inventory="The inventory is empty",
    )

def fuse_characters(first_character: Character, second_character: Character):
    name = first_character.name + " " + second_character.name
    class_name = "Fusion"
    level = (first_character.level + second_character.level) // 2
    strength = (first_character.strength + second_character.strength) * 1.2
    dexterity = (first_character.dexterity + second_character.dexterity) * 1.4
    intelligence = (first_character.intelligence + second_character.intelligence) * 1.5
    hit_points = first_character.hit_points + second_character.hit_points

    if first_character.class_name in ["Mage", "Scout"]:
        inventory = "Bow of the Elven Lords, Amulet of Eternal Wisdom"
    else:
        inventory = "Dragon Scale Armor, Excalibur"

    Character.objects.create(
        name=name,
        class_name=class_name,
        level=level,
        strength=strength,
        dexterity=dexterity,
        intelligence=intelligence,
        hit_points=hit_points,
        inventory=inventory,
    )

    first_character.delete()
    second_character.delete()

def grand_dexterity():
    Character.objects.update(dexterity=30)

def grand_intelligence():
    Character.objects.update(intelligence=40)

def grand_strength():
    Character.objects.update(strength=50)

def delete_characters():
    Character.objects.filter(inventory="The inventory is empty").delete()
