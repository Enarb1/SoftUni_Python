class User:
    def __init__(self, username: str, age: int):
        self.username = username
        self.age = age
        self.movies_liked: list = []
        self.movies_owned: list = []

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        if not value.strip():
            raise ValueError("Invalid username!")
        self.__username = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value < 6:
            raise ValueError("Users under the age of 6 are not allowed!")
        self.__age = value

    def __str__(self):
        result = [f"Username: {self.username}, Age: {self.age}", "Liked movies:"]
        liked_movies = '\n'.join(m.details() for m in self.movies_liked) \
            if len(self.movies_liked) > 0 else "No movies liked."
        result.append(liked_movies)
        result.append("Owned movies:")
        owned_movies = '\n'.join(m.details() for m in self.movies_owned) \
            if len(self.movies_owned) > 0 else "No movies owned."
        result.append(owned_movies)

        return '\n'.join(result)
