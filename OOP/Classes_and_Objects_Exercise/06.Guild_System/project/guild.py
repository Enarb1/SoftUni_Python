from project.player import Player


class Guild:

    def __init__(self, name):
        self.name = name
        self.players = []

    def assign_player(self, player):

        if player not in self.players and player.guild == "Unaffiliated":
            self.players.append(player)
            player.guild = self.name
            return f"Welcome player {player.name} to the guild {self.name}"

        if player in self.players:
            return f"Player {player.name} is already in the guild."

        return f"Player {player.name} is in another guild."

    def kick_player(self, player_name):
        player_to_kick = next((p for p in self.players if p.name == player_name), None)
        if player_to_kick:
            self.players.remove(player_to_kick)
            player_to_kick.guild = "Unaffiliated"
            return f"Player {player_name} has been removed from the guild."

        return f"Player {player_name} is not in the guild."

    def guild_info(self):
        player_data = '\n'.join(p.player_info() for p in self.players)

        return f"Guild: {self.name}\n" \
               f"{player_data}\n"





