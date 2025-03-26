import os
from datetime import date

import django
from django.db.models import Q, Count, Avg, F

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from main_app.models import Movie, Director, Actor


# Create queries within functions


def populate_db():
    director1 = Director.objects.create(
        full_name='Christopher Nolan',
        birth_date='1970-07-30',
        nationality='British-American',
        years_of_experience=25
    )

    director2 = Director.objects.create(
        full_name='Quentin Tarantino',
        birth_date='1963-03-27',
        nationality='American',
        years_of_experience=30
    )

    actor1 = Actor.objects.create(
        full_name='Leonardo DiCaprio',
        birth_date='1974-11-11',
        nationality='American',
        is_awarded=True
    )

    actor2 = Actor.objects.create(
        full_name='Joseph Gordon-Levitt',
        birth_date='1981-02-17',
        nationality='American',
        is_awarded=False
    )

    actor3 = Actor.objects.create(
        full_name='Samuel L. Jackson',
        birth_date='1948-12-21',
        nationality='American',
        is_awarded=True
    )

    actor4 = Actor.objects.create(
        full_name='Margot Robbie',
        birth_date='1990-07-02',
        nationality='Australian',
        is_awarded=False
    )

    movie1 = Movie.objects.create(
        title='Inception',
        release_date=date(2010, 7, 16),
        genre='SCI-FI',
        rating=8.8,
        is_classic=True,
        director=director1,
        starring_actor=actor1,
    )
    movie1.actors.set([actor1, actor2])

    movie2 = Movie.objects.create(
        title='Pulp Fiction',
        release_date=date(1994, 10, 14),
        genre='CRIME',
        rating=8.9,
        is_classic=True,
        director=director2,
        starring_actor=actor3,
    )
    movie2.actors.set([actor3])

    movie3 = Movie.objects.create(
        title='Once Upon a Time in Hollywood',
        release_date=date(2019, 7, 26),
        genre='DRAMA',
        rating=7.6,
        is_classic=False,
        director=director2,
        starring_actor=actor4,
    )
    movie3.actors.set([actor1, actor3, actor4])


def get_directors(search_name=None, search_nationality=None):

    if search_name is None and search_nationality is None:
        return ""

    query = Q()

    if search_name:
        query &= Q(full_name__icontains=search_name)
    if search_nationality:
        query &= Q(nationality__icontains=search_nationality)

    directors = Director.objects.filter(query).order_by('full_name')

    if not directors:
        return ""

    return '\n'.join(f"Director: {d.full_name}, "
                      f"nationality: {d.nationality}, "
                      f"experience: {d.years_of_experience}" for d in directors)

def get_top_director():
    director = Director.objects.get_directors_by_movies_count().first()

    if not director:
        return ""

    return f"Top Director: {director.full_name}, movies: {director.movies_count}."


def get_top_actor():
    actor = Actor.objects.annotate(
        movie_count=Count('starring_movies')).order_by('-movie_count', 'full_name').first()

    if not Movie.objects.all().exists() or not actor:
        return ""

    movies = ", ".join(actor.starring_movies.all().values_list('title', flat=True))
    avg_rating = actor.starring_movies.aggregate(avg_rating=Avg('rating'))['avg_rating'] or 0.0

    return (f"Top Actor: {actor.full_name}, "
            f"starring in movies: {movies}, "
            f"movies average rating: {avg_rating:.1f}")


def get_actors_by_movies_count():

    if not Movie.objects.all().exists():
        return ""

    actors = Actor.objects.annotate(
        movies_count=Count('actor_movies')).order_by('-movies_count', 'full_name')[:3]

    result = []

    for a in actors:
        result.append(f"{a.full_name}, participated in {a.movies_count} movies")

    return "\n".join(result)


def get_top_rated_awarded_movie():
    movie = Movie.objects.filter(is_awarded=True).order_by('-rating', 'title').first()

    if not movie:
        return ""

    starring_actor = movie.starring_actor or "N/A"
    cast = ", ".join(movie.actors.all().order_by('full_name').values_list('full_name', flat=True))

    return (f"Top rated awarded movie: {movie.title}, "
            f"rating: {movie.rating:.1f}. "
            f"Starring actor: {starring_actor}. "
            f"Cast: {cast}.")


def increase_rating():
    updated_movies = Movie.objects.filter(is_classic=True, rating__lt=10.0).update(rating=F('rating') + 0.1)

    if updated_movies == 0:
        return "No ratings increased."

    return f"Rating increased for {updated_movies} movies."
