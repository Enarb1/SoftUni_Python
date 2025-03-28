from project.movie_specification.movie import Movie


class Action(Movie):
    AGE_RESTRICTION_DEFAULT = 12

    def __init__(self, title: str, year: int, owner: object, age_restriction=AGE_RESTRICTION_DEFAULT):
        super().__init__(title, year, owner, age_restriction)

    @property
    def age_restriction(self):
        return self.__age_restriction

    @age_restriction.setter
    def age_restriction(self, value):
        if value < self.AGE_RESTRICTION_DEFAULT:
            raise ValueError(f"Action movies must be restricted for audience "
                             f"under {self.AGE_RESTRICTION_DEFAULT} years!")
        self.__age_restriction = value

    def details(self):
        return f"Action - Title:{self.title}, " \
               f"Year:{self.year}, " \
               f"Age restriction:{self.age_restriction}, " \
               f"Likes:{self.likes}, " \
               f"Owned by:{self.owner.username}"