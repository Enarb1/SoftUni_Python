from project.battleships.base_battleship import BaseBattleship
from project.battleships.pirate_battleship import PirateBattleship
from project.battleships.royal_battleship import RoyalBattleship
from project.zones.base_zone import BaseZone
from project.zones.pirate_zone import PirateZone
from project.zones.royal_zone import RoyalZone


class BattleManager:
    valid_zones = {
        "RoyalZone": RoyalZone,
        "PirateZone": PirateZone
    }

    valid_ships = {
        "RoyalBattleship": RoyalBattleship,
        "PirateBattleship": PirateBattleship
    }

    ship_zones = {
        "RoyalBattleship": "RoyalZone",
        "PirateBattleship": "PirateZone"
    }


    def __init__(self):
        self.zones = []
        self.ships = []


    def add_zone(self, zone_type: str, zone_code: str) -> str:
        try:
            zone = self.valid_zones[zone_type](zone_code)
        except KeyError:
            raise Exception (f"Invalid zone type!")

        try:
            existing_zones = next(filter(lambda z: z.code == zone_code, self.zones))
            raise Exception (f"Zone already exists!")
        except StopIteration:

            self.zones.append(zone)
            return f"A zone of type {zone_type} was successfully added."


    def add_battleship(self, ship_type: str, name: str, health: int, hit_strength: int) -> str:
        try:
            battleship = self.valid_ships[ship_type](name, health, hit_strength)
        except KeyError:
           raise Exception(f"{ship_type} is an invalid type of ship!")

        self.ships.append(battleship)
        return f"A new {ship_type} was successfully added."


    def add_ship_to_zone(self, zone: BaseZone, ship: BaseBattleship):
        if zone.volume <= 0:
            return f"Zone {zone.code} does not allow more participants!"

        if ship.health <= 0:
            return f"Ship {ship.name} is considered sunk! Participation not allowed!"

        if not ship.is_available:
            return f"Ship {ship.name} is not available and could not participate!"

        if self.ship_zones[ship.__class__.__name__] == zone.__class__.__name__:
            ship.is_attacking = True

        ship.is_available = False
        zone.ships.append(ship)
        zone.volume -= 1

        return f"Ship {ship.name} successfully participated in zone {zone.code}."

    def remove_battleship(self, ship_name: str):
        try:
            ship = next(filter(lambda s: s.name == ship_name, self.ships))
        except StopIteration:
            return "No ship with this name!"

        if not ship.is_available:
            return f"The ship participates in zone battles! Removal is impossible!"

        self.ships.remove(ship)

        return f"Successfully removed ship {ship_name}."


    def start_battle(self, zone: BaseZone):

        ships_in_attack = [s for s in zone.ships if s.is_attacking]
        ships_in_defense = [s for s in zone.ships if not s.is_attacking]

        if not ships_in_attack or not ships_in_defense:
            return "Not enough participants. The battle is canceled."

        attacking_ship = sorted(ships_in_attack, key=lambda s: s.hit_strength)[-1]
        defending_ship = sorted(ships_in_defense, key=lambda s: s.health)[-1]

        attacking_ship.attack()
        defending_ship.take_damage(attacking_ship)

        if defending_ship.health <= 0:
            zone.ships.remove(defending_ship)
            self.ships.remove(defending_ship)
            return f"{defending_ship.name} lost the battle and was sunk."

        if attacking_ship.ammunition <= 0:
            zone.ships.remove(attacking_ship)
            self.ships.remove(attacking_ship)
            return f"{attacking_ship.name} ran out of ammunition and leaves."


        return "Both ships survived the battle."

    def get_statistics(self):
        available_ships = [s for s in self.ships if s.is_available]
        message = f"Available Battleships: {len(available_ships)}"

        if available_ships:
            message += "\n#" + ", ".join(f"{s.name}" for s in available_ships) + "#"

        sorted_zones = sorted(self.zones, key=lambda z: z.code)
        message += f"\n***Zones Statistics:***\nTotal Zones: {len(self.zones)}\n"

        for zone in sorted_zones:
            message += zone.zone_info() + "\n"

        return message
