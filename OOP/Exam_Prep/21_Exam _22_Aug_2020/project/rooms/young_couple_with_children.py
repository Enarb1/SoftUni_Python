from project.appliances.fridge import Fridge
from project.appliances.laptop import Laptop
from project.appliances.tv import TV
from project.rooms.room import Room


class YoungCoupleWithChildren(Room):
    def __init__(self, family_name: str, salary_one: float, salary_two: float, *children):
        total_budget = salary_one + salary_two
        members_count = 2 + len(children)
        super().__init__(family_name, total_budget, members_count)
        self.room_cost = 30
        self.children.extend(children)
        self.appliances = [TV(), Fridge(), Laptop()] * members_count
        args = []
        args.extend(self.children)
        args.extend(self.appliances)
        self.calculate_expenses(args)
