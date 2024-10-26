from project.zones.base_zone import BaseZone


class RoyalZone(BaseZone):
    INITIAL_VOLUME = 10
    def __init__(self, code: str):
        super().__init__(code, self.INITIAL_VOLUME)

    def zone_info(self):
        ships = self.get_ships()
        message= (f"@Royal Zone Statistics@\n"
                  f"Code: {self.code}; Volume: {self.volume}\n"
                  f"Battleships currently in the Royal Zone: {len(self.ships)}, "
                  f"{len([s for s in self.ships if s.__class__.__name__ == 'PirateBattleship'])} "
                  f"out of them are Pirate Battleships.")

        if ships:
            message += "\n#" + ", ".join(f"{b.name}" for b in ships) + "#"

        return message
