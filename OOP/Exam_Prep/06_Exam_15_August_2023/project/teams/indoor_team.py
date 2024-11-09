from project.teams.base_team import BaseTeam


class IndoorTeam(BaseTeam):
    INITIAL_BUDGET = 500.0
    ADVANTAGE_INCREASE = 145

    def __init__(self,  name, country, advantage):
        super().__init__(name, country, advantage, IndoorTeam.INITIAL_BUDGET)


    def win(self):
        self.advantage += IndoorTeam.ADVANTAGE_INCREASE
        self.wins += 1