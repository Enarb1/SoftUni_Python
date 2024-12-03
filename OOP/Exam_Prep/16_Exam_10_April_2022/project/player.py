class Player:
    players_names = []
    AGE_RESTRICTION = 12
    MAX_STAMINA = 100

    def __init__(self, name: str, age: int, stamina=MAX_STAMINA):
        self.name = name
        self.age = age
        self.stamina = stamina

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value.strip():
            raise ValueError("Name not valid!")
        if value in Player.players_names:
            raise Exception(f"Name {value} is already used!")
        self.players_names.append(value)
        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value < self.AGE_RESTRICTION:
            raise ValueError(f"The player cannot be under {self.AGE_RESTRICTION} years old!")
        self.__age = value

    @property
    def stamina(self):
        return self.__stamina

    @stamina.setter
    def stamina(self, value):
        if value < 0 or value > 100:
            raise ValueError("Stamina not valid!")
        self.__stamina = value

    @property
    def need_sustenance(self):
        return self.__stamina < self.MAX_STAMINA

    def _sustain_player(self, energy):
        if self.stamina + energy > self.MAX_STAMINA:
            self.stamina = 100
        else:
            self.stamina += energy

    def __str__(self):
        return f"Player: {self.name}, {self.age}, {self.stamina}, {self.need_sustenance}"
