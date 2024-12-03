from project.player import Player
from project.supply.supply import Supply
from project.supply.drink import Drink
from project.supply.food import Food


class Controller:
    VALID_SUPPLY_TYPES = ["Food", "Drink"]

    def __init__(self):
        self.players: list = []
        self.supplies: list = []

    def add_player(self, *players):
        added_players = []
        for p in players:
            if p not in self.players:
                self.players.append(p)
                added_players.append(p.name)
        return f"Successfully added: {', '.join(added_players)}"

    def add_supply(self, *supplies):
        self.supplies.extend(supplies)

    def sustain(self, player_name: str, sustenance_type: str):
        player = self.__get_player(player_name)
        if player is not None:
            if player.stamina == 100:
                return f"{player.name} have enough stamina."
            if sustenance_type in self.VALID_SUPPLY_TYPES:
                supply = self.__get_supply(sustenance_type)
                player._sustain_player(supply.energy)
                return f"{player.name} sustained successfully with {supply.name}."

    def duel(self, first_player_name: str, second_player_name: str):
        player1 = self.__get_player(first_player_name)
        player2 = self.__get_player(second_player_name)

        result = self.__check_for_stamina(player1, player2)
        if result:
            return result
        rank_by_stamina = sorted([player1, player2], key=lambda p: p.stamina)
        attacker = rank_by_stamina[0]
        defender = rank_by_stamina[-1]
        winner = self.__fight(attacker, defender)
        return f"Winner: {winner.name}"

    def next_day(self):
        self.__reduce_stamina()
        self.__feed_players()

    def __str__(self):
        info = []
        for p in self.players:
            info.append(p.__str__())
        for s in self.supplies:
            info.append(s.details())
        return "\n".join(info)

    @staticmethod
    def __fight(first_attacker, second_attacker):
        attacker = first_attacker
        defending = second_attacker
        winner = None
        for _ in range(2):
            if defending.stamina - (attacker.stamina / 2) < 0:
                defending.stamina = 0
                winner = attacker
                break
            else:
                defending.stamina -= (attacker.stamina / 2)
            attacker = second_attacker
            defending = first_attacker

        if winner is None:
            winner = max([attacker, defending], key=lambda p: p.stamina)
        return winner

    @staticmethod
    def __check_for_stamina(*players):
        result = []
        for p in players:
            if p.stamina == 0:
                result.append(f"Player {p.name} does not have enough stamina.")
        if result:
            return '\n'.join(result)

    def __get_supply(self, sustenance_type):
        for i in range(len(self.supplies) - 1, 1, -1):
            if type(self.supplies[i]).__name__ == sustenance_type:
                return self.supplies.pop(i)
        raise Exception(f"There are no {sustenance_type} supplies left!")

    def __get_player(self, player_name):
        return next((p for p in self.players if p.name == player_name), None)

    def __reduce_stamina(self):
        for p in self.players:
            if p.stamina - (p.age * 2) < 0:
                p.stamina = 0
            else:
                p.stamina -= (p.age * 2)

    def __feed_players(self):
        for p in self.players:
            self.sustain(p.name, "Food")
            self.sustain(p.name, "Drink")
