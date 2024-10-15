def movie_organizer(*movies):

    collection = {}

    for movie, genre in sorted(movies):
        if genre not in collection.keys():
            collection[genre] = []
        collection[genre].append(movie)

    sorted_collection = sorted(collection.items(), key=lambda x: ((-len(x[1])),x[0]))

    final_print = ""

    for genre, movies in sorted_collection:
        final_print += f"{genre} - {len(movies)}\n"
        for movie in movies:
            final_print += f"* {movie}\n"

    return final_print


print(movie_organizer(
    ("The Matrix", "Sci-fi")))