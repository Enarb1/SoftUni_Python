movies_count = int(input())

max_rating = float("-inf")
min_rating = float("inf")
movie_max_rating = ""
movie_min_rating = ""
ratings_total = 0

for _ in range(movies_count):
    movie = input()
    rating = float(input())
    if rating > max_rating:
        max_rating = rating
        movie_max_rating = movie
    if rating < min_rating:
        min_rating = rating
        movie_min_rating = movie
    ratings_total += rating

print(f"{movie_max_rating} is with highest rating: {max_rating:.1f}")
print(f"{movie_min_rating} is with lowest rating: {min_rating:.1f}")
print(f"Average rating: {ratings_total / movies_count:.1f}")
