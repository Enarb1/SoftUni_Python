import os
import django
from django.db.models import Q, Count, Avg, F

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from main_app.models import Actor, Director, Movie
# Create queries within functions

def populate_db():
    director1 = Director.objects.create(
        full_name="Christopher Nolan",
        birth_date="1970-07-30",
        nationality="British-American",
        years_of_experience=25,
    )

    director1.save()
    director2 = Director.objects.create(
        full_name="Quentin Tarantino",
        birth_date="1963-03-27",
        nationality="American",
        years_of_experience=30,
    )
    director2.save()

    actor1 = Actor.objects.create(
        full_name="Leonardo DiCaprio",
        birth_date="1974-11-11",
        nationality="American",
        is_awarded=True,
    )
    actor1.save()
    actor2 = Actor.objects.create(
        full_name="Christian Bale",
        birth_date="1974-01-30",
        nationality="British",
        is_awarded=True,
    )
    actor2.save()
    actor3 = Actor.objects.create(
        full_name="Brad Pitt",
        birth_date="1963-12-18",
        nationality="American",
        is_awarded=True,
    )
    actor3.save()
    movie1 = Movie.objects.create(
        title="Inception",
        release_date="2010-07-16",
        storyline="A skilled thief, the absolute best in the dangerous art of extraction...",
        genre=Movie.MovieGenreChoices.ACTION,
        rating=8.8,
        is_classic=True,
        director=director1,
        starring_actor=actor1,
    )
    movie1.save()
    movie2 = Movie.objects.create(
        title="The Dark Knight",
        release_date="2008-07-18",
        storyline="When the menace known as The Joker emerges from his mysterious past...",
        genre=Movie.MovieGenreChoices.ACTION,
        rating=9.0,
        is_classic=True,
        director=director1,
        starring_actor=actor2,
    )
    movie2.save()
    movie3 = Movie.objects.create(
        title="Once Upon a Time in Hollywood",
        release_date="2019-07-26",
        storyline="A faded television actor and his stunt double strive to achieve fame...",
        genre=Movie.MovieGenreChoices.DRAMA,
        rating=7.6,
        is_classic=False,
        director=director2,
        starring_actor=actor3,
    )
    movie3.save()

    movie1.actors.set([actor1, actor2])
    movie2.actors.set([actor1, actor2])
    movie3.actors.set([actor1, actor3])

def get_directors(search_name=None, search_nationality=None):
    if search_name is None and search_nationality is None:
        return ""

    query = Q()

    if search_name:
        query &= Q(full_name__icontains=search_name)
    if search_nationality:
        query &= Q(nationality__icontains=search_nationality)

    if not Director.objects.filter(query).exists():
        return ""

    directors = Director.objects.filter(query).order_by("full_name")

    result = []
    for director in directors:
        result.append(
            f"Director: {director.full_name}, "
            f"nationality: { director.nationality},"
            f" experience: {director.years_of_experience}"
        )
    return "\n".join(result)


def get_top_director():

    if not Director.objects.get_directors_by_movies_count().exists():
        return ""

    director = Director.objects.get_directors_by_movies_count().first()

    return f"Top Director: {director.full_name}, movies: {director.movies_count}."

def get_top_actor():
    actor = Actor.objects.prefetch_related('starring_movies').annotate(
        movie_count=Count("starring_movies"),
        avg_rating=Avg("starring_movies__rating"),
    ).order_by("-movie_count", "full_name").first()

    if not actor or not actor.movie_count:
        return ""

    movies = ", ".join(m.title for m in actor.starring_movies.all() if m)

    return (f"Top Actor: {actor.full_name}, starring in movies: {movies}, "
            f"movies average rating: {actor.avg_rating:.1f}")

def get_actors_by_movies_count():
    actors = Actor.objects.annotate(
        movies_count=Count("actor_movies")).order_by("-movies_count","full_name")[:3]

    if not actors or not actors[0].movies_count:
        return ""

    result = []

    for a in actors:
        result.append(
            f"{a.full_name}, participated in {a.movies_count} movies"
        )

    return "\n".join(result)

def get_top_rated_awarded_movie():
    top_movie = Movie.objects.select_related("starring_actor").prefetch_related('actors').filter(
        is_awarded=True).order_by('-rating', 'title').first()

    if top_movie is None:
        return ""

    starring_actor = top_movie.starring_actor.full_name if top_movie.starring_actor else "N/A"
    movie_actors = top_movie.actors.order_by('full_name').values_list("full_name", flat=True)

    cast = ", ".join(movie_actors)

    return (f"Top rated awarded movie: {top_movie.title}, "
            f"rating: {top_movie.rating}. "
            f"Starring actor: {starring_actor}. "
            f"Cast: {cast}.")

def increase_rating():
    movies_to_update = Movie.objects.filter(is_classic=True, rating__lt=10)

    if not movies_to_update:
        return "No ratings increased."

    updated_movies_count = movies_to_update.count()
    movies_to_update.update(rating=F('rating') + 0.1)

    return f"Rating increased for {updated_movies_count} movies."

