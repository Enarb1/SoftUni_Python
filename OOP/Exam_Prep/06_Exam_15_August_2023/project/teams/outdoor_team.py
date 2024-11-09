from project.teams.base_team import BaseTeam

class OutdoorTeam(BaseTeam):
    INITIAL_BUDGET = 1000.0
    ADVANTAGE_INCREASE = 115

    def __init__(self,  name, country, advantage):
        super().__init__(name, country, advantage, OutdoorTeam.INITIAL_BUDGET)


    def win(self):
        self.advantage += OutdoorTeam.ADVANTAGE_INCREASE
        self.wins += 1