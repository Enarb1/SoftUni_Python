import os
import django
from django.db.models import Q, Count, Avg

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from main_app.models import Author, Article, Review
# Create queries within functions

def get_authors(search_name=None, search_email=None):

    if not search_name and not search_email:
        return ""

    query = Q()

    if search_name:
        query &= Q(full_name__icontains=search_name)
    if search_email:
        query &= Q(email__icontains=search_email)

    authors = Author.objects.filter(query).order_by("-full_name")

    if not authors:
        return ""

    result = []

    for a in authors:
        status = "Banned" if a.is_banned else "Not Banned"
        result.append(f"Author: {a.full_name}, email: {a.email}, status: {status}")

    return "\n".join(result)

def get_top_publisher():
    top_author = Author.objects.get_authors_by_article_count().first()

    if not Article.objects.exists():
        return ""

    return f"Top Author: {top_author.full_name} with {top_author.articles_count} published articles."

def get_top_reviewer():
    top_reviewer = Review.objects.values(
        'author__full_name', 'author__email',
    ). annotate(reviews_count=Count('id')
                ). order_by('-reviews_count', 'author__email').first()

    if not top_reviewer:
        return ""

    return f"Top Reviewer: {top_reviewer['author__full_name']} with {top_reviewer['reviews_count']} published reviews."

def get_latest_article():

    if not Article.objects.exists():
        return ""

    last_article = Article.objects.order_by("-published_on").first()

    authors = ", ".join(last_article.authors.order_by("full_name").values_list("full_name", flat=True))
    avg_rating = last_article.reviews.aggregate(Avg("rating"))["rating__avg"] or 0


    return (f"The latest article is: {last_article.title}. "
            f"Authors: {authors}. "
            f"Reviewed: {last_article.reviews.count()} times. "
            f"Average Rating: {avg_rating:.2f}.")

def get_top_rated_article():

    top_article = (
        Article.objects.annotate(
            avg_rating=Avg("reviews__rating", filter=Q(reviews__published_on__isnull=False)),
            review_count=Count("reviews", filter=Q(reviews__published_on__isnull=False))
        )
        .filter(avg_rating__isnull=False)
        .order_by("-avg_rating", "title")
        .first()
    )

    if not top_article:
        return ""

    return (f"The top-rated article is: {top_article.title}, "
            f"with an average rating of {top_article.avg_rating:.2f}, "
            f"reviewed {top_article.review_count} times.")

def ban_author(email=None):

    if not email or not Author.objects.filter(email=email) or not Author.objects.all().exists():
        return "No authors banned."

    author = Author.objects.get(email=email)
    reviews_count = author.reviews.count()
    author.reviews.all().delete()
    author.is_banned = True
    author.save()

    return f"Author: {author.full_name} is banned! {reviews_count} reviews deleted."
