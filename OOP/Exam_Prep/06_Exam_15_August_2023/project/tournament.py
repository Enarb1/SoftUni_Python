from project.equipment.knee_pad import KneePad
from project.equipment.elbow_pad import ElbowPad
from project.teams.outdoor_team import OutdoorTeam
from project.teams.indoor_team import IndoorTeam

class Tournament:

    VALID_EQUIPMENT_TYPES = {
        "KneePad": KneePad,
        "ElbowPad": ElbowPad
    }

    VALID_TEAM_TYPES = {
        "OutdoorTeam": OutdoorTeam,
        "IndoorTeam": IndoorTeam
    }


    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.equipment: list = []
        self.teams: list = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value.isalnum():
            raise ValueError("Tournament name should contain letters and digits only!")

        self.__name = value

    def add_equipment(self, equipment_type: str) -> str:
        if equipment_type not in self.VALID_EQUIPMENT_TYPES.keys():
            raise Exception("Invalid equipment type!")

        new_equipment = self.VALID_EQUIPMENT_TYPES[equipment_type]()
        self.equipment.append(new_equipment)

        return f"{equipment_type} was successfully added."


    def add_team(self, team_type: str, team_name: str, country: str, advantage: int) -> str:
        if team_type not in self.VALID_TEAM_TYPES.keys():
            raise Exception("Invalid team type!")

        if len(self.teams) >= self.capacity:
            return "Not enough tournament capacity."

        new_team = self.VALID_TEAM_TYPES[team_type](team_name, country, advantage)
        self.teams.append(new_team)

        return f"{team_type} was successfully added."


    def sell_equipment(self, equipment_type: str, team_name: str) -> str:
        equipment_for_sale = self._get_equipment(equipment_type)[-1]
        team = self._get_team(team_name)

        if team.budget < equipment_for_sale.price:
            raise Exception("Budget is not enough!")

        team.equipment.append(equipment_for_sale)
        team.budget -= equipment_for_sale.price
        self.equipment.remove(equipment_for_sale)

        return f"Successfully sold {equipment_type} to {team_name}."


    def remove_team(self, team_name: str):
        team = self._get_team(team_name)

        if team is None:
            raise Exception("No such team!")

        if team.wins > 0:
            raise Exception(f"The team has {team.wins} wins! Removal is impossible!")

        self.teams.remove(team)

        return f"Successfully removed {team_name}."


    def increase_equipment_price(self, equipment_type: str) -> str:
        equipment_for_price_increase = self._get_equipment(equipment_type)

        for e in equipment_for_price_increase:
            e.increase_price()

        return f"Successfully changed {len(equipment_for_price_increase)}pcs of equipment."


    def play(self, team_name1: str, team_name2: str):
        team_one = self._get_team(team_name1)
        team_two = self._get_team(team_name2)

        if team_one.__class__.__name__ != team_two.__class__.__name__:
            raise Exception("Game cannot start! Team types mismatch!")

        team_one_points = team_one.advantage + team_one.get_average_protection()
        team_two_points = team_two.advantage + team_two.get_average_protection()

        if team_one_points != team_two_points:
            winner = team_one if team_one_points > team_two_points else team_two
            winner.win()
            return f"The winner is {winner.name}."

        return "No winner in this game."


    def get_statistics(self):
        sorted_teams = sorted(self.teams, key=lambda t: -t.wins)
        result = [
            f"Tournament: {self.name}\n"
            f"Number of Teams: {len(self.teams)}\n"
            f"Teams:"
        ]
        [result.append(t.get_statistics()) for t in sorted_teams]

        return '\n'.join(result)


    def _get_team(self, team_name: str):

        team = [t for t in self.teams if t.name == team_name]
        return team[0] if team else None


    def _get_equipment(self, equipment_type: str) -> list:
        return [e for e in self.equipment if e.__class__.__name__ == equipment_type]

