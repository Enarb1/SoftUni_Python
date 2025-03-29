import os
from datetime import date

import django
from django.db.models import Q, Count, Avg, F

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from main_app.models import Publisher, Author, Book


# Create queries within functions


def populate_db():
    epic_reads = Publisher.objects.create(
        name="Epic Reads",
        country="US",
        established_date=date(1923, 5, 15),
        rating=4.94,
    )

    global_prints = Publisher.objects.create(
        name="Global Prints",
        country="Australia",
    )

    abrams_books = Publisher.objects.create(
        name="Abrams Books",
        rating=1.05,
    )

    jack_london = Author.objects.create(
        name="Jack London",
        country="US",
        birth_date=date(1876, 1, 12),
        is_active=False,
    )

    craig_richardson = Author.objects.create(
        name="Craig Richardson",
    )

    ramsey_hamilton = Author.objects.create(
        name="Ramsey Hamilton",
    )

    luciano_ramalho = Author.objects.create(
        name="Luciano Ramalho",
    )

    Book.objects.create(
        title="Adventures in Python",
        publication_date=date(2015, 6, 1),
        summary="An engaging and detailed guide to mastering a popular programming language.",
        genre="Non-Fiction",
        price=49.99,
        rating=4.8,
        publisher=epic_reads,
        main_author=craig_richardson,
    ).co_authors.set([ramsey_hamilton])

    Book.objects.create(
        title="The Call of the Wild",
        publication_date=date(1903, 11, 23),
        summary="A classic fiction adventure story set during the Klondike Gold Rush.",
        genre="Fiction",
        price=29.99,
        rating=4.9,
        is_bestseller=True,
        publisher=global_prints,
        main_author=jack_london,
    )

    Book.objects.create(
        title="Django World",
        publication_date=date(2025, 1, 1),
        summary="A comprehensive resource for advanced users of a web development framework.",
        genre="Non-Fiction",
        price=89.99,
        rating=5.0,
        publisher=epic_reads,
        main_author=craig_richardson,
    ).co_authors.set([luciano_ramalho, ramsey_hamilton])

    Book.objects.create(
        title="Integration Testing",
        publication_date=date(2024, 12, 31),
        summary="A thorough exploration of expert-level testing strategies.",
        genre="Non-Fiction",
        price=89.99,
        rating=4.89,
        is_bestseller=True,
        publisher=epic_reads,
        main_author=ramsey_hamilton,
    )

    Book.objects.create(
        title="Unit Testing",
        publication_date=date(2025, 2, 1),
        summary="A detailed guide to foundational testing principles.",
        genre="Non-Fiction",
        price=90.00,
        rating=3.99,
        publisher=epic_reads,
        main_author=craig_richardson,
    ).co_authors.set([ramsey_hamilton])


def get_publishers(search_string=None):

    if search_string is None:
        return "No search criteria."

    query = Q(name__icontains=search_string) | Q(country__icontains=search_string)
    publishers = Publisher.objects.filter(query).order_by("-rating", "name")

    if not publishers:
        return "No publishers found."

    result = []

    for p in publishers:
        country = p.country if p.country != "TBC" else "Unknown"
        result.append(f"Publisher: {p.name}, country: {country}, rating: {p.rating:.1f}")

    return "\n".join(result)


def get_top_publisher():
    top_p = Publisher.objects.get_publishers_by_books_count().first()

    if not top_p:
        return "No publishers found."

    return f"Top Publisher: {top_p.name} with {top_p.books_count} books."


def get_top_main_author():

    if not Author.objects.all().exists() or not Book.objects.all().exists():
        return "No results."

    author = Author.objects.annotate(books_count=Count("books")).order_by("-books_count", "name").first()

    books = ", ".join(author.books.all().order_by("title").values_list("title", flat=True))
    avg_rating = author.books.aggregate(Avg("rating"))["rating__avg"]

    return (f"Top Author: {author.name}, "
            f"own book titles: {books}, "
            f"books average rating: {avg_rating:.1f}")


def get_authors_by_books_count():

    if not Author.objects.all().exists() or not Book.objects.all().exists():
        return "No results."

    authors = Author.objects.annotate(
        main_books_count=Count('books', distinct=True),
        coauthored_books_count=Count('coauthored_books', distinct=True),
    ).annotate(
        total_books_count=F('main_books_count') + F('coauthored_books_count')
    ).order_by("-total_books_count", "name")[:3]

    result = []

    for a in authors:
        result.append(f"{a.name} authored {a.total_books_count} books.")

    return "\n".join(result)


def get_top_bestseller():

    bestseller = Book.objects.filter(is_bestseller=True).order_by("-rating", "title").first()

    if not bestseller:
        return "No results."

    co_authors = ", ".join(bestseller.co_authors.all().order_by("name").values_list("name", flat=True)) or "N/A"

    return (f"Top bestseller: {bestseller.title},"
            f" rating: {bestseller.rating:.1f}. "
            f"Main author: {bestseller.main_author.name}. "
            f"Co-authors: {co_authors}.")


def increase_price():

    updated_books = Book.objects.filter(publication_date__year=2025, rating__gte=4.0).update(price=F("price") * 1.2)

    if updated_books == 0:
        return "No changes in price."

    return f"Prices increased for {updated_books} books."
