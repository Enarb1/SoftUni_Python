from project.zones.base_zone import BaseZone


class PirateZone(BaseZone):
    INITIAL_VOLUME = 8
    def __init__(self, code: str):
        super().__init__(code,self.INITIAL_VOLUME)

    def zone_info(self):
        ships = self.get_ships()
        message = (f"@Pirate Zone Statistics@\n"
                f"Code: {self.code}; Volume: {self.volume}\n"
                 f"Battleships currently in the Pirate Zone: {len(self.ships)}, "
                   f"{len([s for s in self.ships if s.__class__.__name__ == 'RoyalBattleship'])}"
                   f" out of them are Royal Battleships.")

        if ships:
            message += "\n#" + ", ".join(f"{b.name}" for b in ships) + "#"

        return message