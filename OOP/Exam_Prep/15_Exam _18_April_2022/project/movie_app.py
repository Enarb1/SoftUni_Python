from project.user import User
from project.movie_specification.movie import Movie
from project.movie_specification.action import Action
from project.movie_specification.fantasy import Fantasy
from project.movie_specification.thriller import Thriller


class MovieApp:
    def __init__(self):
        self.movies_collection: list = []
        self.users_collection: list = []

    def register_user(self, username: str, age: int):
        if self.__get_user(username) is not None:
            raise Exception("User already exists!")
        user = User(username, age)
        self.users_collection.append(user)
        return f"{user.username} registered successfully."

    def upload_movie(self, username: str, movie):
        user = self.__get_user(username)
        if user is None:
            raise Exception("This user does not exist!")
        if user.username != movie.owner.username:
            raise Exception(f"{user.username} is not the owner of the movie {movie.title}!")
        if self.__get_movie(movie) is not None:
            raise Exception("Movie already added to the collection!")

        user.movies_owned.append(movie)
        self.movies_collection.append(movie)
        return f"{user.username} successfully added {movie.title} movie."

    def edit_movie(self, username: str, movie: Movie, **kwargs):
        user = self.__get_user(username)
        self.__is_movie_uploaded(movie)
        self.__is_movie_owner(user, movie)

        for attribute, value in kwargs.items():
            setattr(movie, attribute, value)

        return f"{user.username} successfully edited {movie.title} movie."

    def delete_movie(self, username: str, movie: Movie):
        user = self.__get_user(username)
        self.__is_movie_uploaded(movie)
        self.__is_movie_owner(user, movie)

        user.movies_owned.remove(movie)
        self.movies_collection.remove(movie)
        return f"{user.username} successfully deleted {movie.title} movie."

    def like_movie(self, username: str, movie: Movie):
        user = self.__get_user(username)
        if user.username == movie.owner.username:
            raise Exception(f"{user.username} is the owner of the movie {movie.title}!")
        if movie in user.movies_liked:
            raise Exception(f"{user.username} already liked the movie {movie.title}!")

        movie.likes += 1
        user.movies_liked.append(movie)
        return f"{user.username} liked {movie.title} movie."

    def dislike_movie(self, username: str, movie: Movie):
        user = self.__get_user(username)
        if movie not in user.movies_liked:
            raise Exception(f"{user.username} has not liked the movie {movie.title}!")
        user.movies_liked.remove(movie)
        movie.likes -= 1

        return f"{user.username} disliked {movie.title} movie."

    def display_movies(self):
        sorted_movies = sorted(self.movies_collection, key=lambda m: (-m.year, m.title))
        if not self.movies_collection:
            return "No movies found."
        result = '\n'.join(m.details() for m in sorted_movies)
        return result

    def __str__(self):
        users = ', '.join(u.username for u in self.users_collection) if self.users_collection else "No users."
        movies = ', '.join(m.title for m in self.movies_collection) if self.movies_collection else "No movies."
        return f"All users: {users}\nAll movies: {movies}"

    @staticmethod
    def __is_movie_owner(user, movie):
        if user.username != movie.owner.username:
            raise Exception(f"{user.username} is not the owner of the movie {movie.title}!")

    def __is_movie_uploaded(self, movie):
        if self.__get_movie(movie) is None:
            raise Exception(f"The movie {movie.title} is not uploaded!")

    def __get_movie(self, movie):
        return next((m for m in self.movies_collection if m.title == movie.title), None)

    def __get_user(self, username):
        return next((u for u in self.users_collection if u.username == username), None)



