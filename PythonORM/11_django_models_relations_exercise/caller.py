import os
from datetime import date, timedelta

import django
from django.db.models import Avg

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from main_app.models import (Author, Book, Artist, Song, Product, Review, Driver, DrivingLicense, Owner, Car,
                             Registration)
# Create queries within functions

def show_all_authors_with_their_books():
    result = []
    authors = Author.objects.all().order_by('id')

    for a in authors:
        books = Book.objects.filter(author=a)
        if not books:
            continue

        titles = ", ".join(b.title for b in books)
        result.append(
            f"{a.name} has written - {titles}!"
        )

    return "\n".join(result)

def delete_all_authors_without_books():
    Author.objects.filter(book__isnull=True).delete()


def add_song_to_artist(artist_name: str, song_title: str):
    artist = Artist.objects.get(name=artist_name)
    song = Song.objects.get(title=song_title)
    artist.songs.add(song)

def get_songs_by_artist(artist_name: str):
    return Artist.objects.get(name=artist_name).songs.all().order_by("-id")

def remove_song_from_artist(artist_name: str, song_title: str):
    artist = Artist.objects.get(name=artist_name)
    song = Song.objects.get(title=song_title)

    artist.songs.remove(song)

def calculate_average_rating_for_product_by_name(product_name: str):
    product = Product.objects.get(name=product_name)
    reviews = product.reviews.all()

    return sum(r.rating for r in reviews) / len(reviews)

    # product = Product.objects.annotate(
    #     average_rating=Avg("reviews__rating"),
    # ).get(name=product_name)
    #
    # return product.average_rating

def get_reviews_with_high_ratings(threshold: int):
    return Review.objects.filter(rating__gte=threshold)

def get_products_with_no_reviews():
    return Product.objects.filter(reviews__isnull=True).order_by("-name")

def delete_products_without_reviews():
    get_products_with_no_reviews().delete()

def calculate_licenses_expiration_dates():
    licenses = DrivingLicense.objects.order_by("-license_number")

    return "\n".join(str(l) for l in licenses)

def get_drivers_with_expired_licenses(due_date: date):
    cutoff_date = due_date - timedelta(days=365)

    return Driver.objects.filter(
        license__issue_date__gt=cutoff_date
    )


def register_car_by_owner(owner: Owner):
    registration = Registration.objects.filter(car__isnull=True).first()
    car = Car.objects.filter(registration__isnull=True).first()

    car.owner = owner
    car.save()

    registration.registration_date = date.today()
    registration.car = car
    registration.save()

    return (f"Successfully registered {car.model} to "
            f"{owner.name} with registration number {registration.registration_number}.")


"""This functions are added by me and are not in the task"""

def unregister_car(car_id: int):

    Car.objects.filter(id=car_id).update(owner=None)

def register_car(owner: Owner, car: Car):
    pass

def change_car_owner(registration_number: str, new_owner: Owner):
    car = Car.objects.filter(registration__registration_number=registration_number).first()
    old_owner = Owner.objects.filter(
        cars__registration__registration_number=registration_number
    ).values_list('name', flat=True).first()

    unregister_car(car.id)

    car.owner = new_owner
    car.save()

    return (f"Successfully registered transferred the car {car.model} with registration number {registration_number} "
            f"from {old_owner} to {str(new_owner)}.")


# buyer = Owner.objects.get(id=1)
#
# print(change_car_owner("TX0044XA", buyer))










