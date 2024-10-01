class Player:

    def __init__(self, name, hp, mp, guild="Unaffiliated"):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.skills = {}
        self.guild = guild

    def add_skill(self, skill_name, mana_cost):
        if skill_name not in self.skills.keys():
            self.skills[skill_name] = mana_cost
            return f"Skill {skill_name} added to the collection of the player {self.name}"

        return "Skill already added"

    def player_info(self):
        skills_print = '\n'.join(f"==={s} - {m}" for s, m in self.skills.items())
        return f"Name: {self.name}\n" \
               f"Guild: {self.guild}\n" \
               f"HP: {self.hp}\n" \
               f"MP: {self.mp}\n" \
               f"{skills_print}\n"
