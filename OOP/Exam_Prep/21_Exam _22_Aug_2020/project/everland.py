from project.rooms.alone_old import AloneOld
from project.rooms.alone_young import AloneYoung
from project.rooms.old_couple import OldCouple
from project.rooms.young_couple import YoungCouple
from project.rooms.young_couple_with_children import YoungCoupleWithChildren
from project.people.child import Child


class Everland:
    def __init__(self):
        self.rooms: list = []

    def add_room(self, room):
        self.rooms.append(room)

    def get_monthly_consumptions(self):
        total_cost = 0
        for r in self.rooms:
            total_cost += self.__calculate_cost_for_one_room(r)
        return f"Monthly consumption: {total_cost:.2f}$."

    def pay(self):
        result = []
        rooms_to_remove = []

        for room in self.rooms:
            total_expenses = self.__calculate_cost_for_one_room(room)
            if room.budget >= total_expenses:
                room.budget -= total_expenses
                result.append(f"{room.family_name} paid {total_expenses:.2f}$ and have {room.budget:.2f}$ left.")
            else:
                rooms_to_remove.append(room)
                result.append(f"{room.family_name} does not have enough budget and must leave the hotel.")
        self.__remove_rooms(rooms_to_remove)
        return "\n".join(result)

    def status(self):
        total_people = sum(r.members_count for r in self.rooms)
        result = [f"Total population: {total_people}"]

        for room in self.rooms:
            result.append(f"{room.family_name} with {room.members_count} members. "
                          f"Budget: {room.budget:.2f}$, Expenses: {room.expenses:.2f}$")
            if room.children:
                for n, child in enumerate(room.children):
                    result.append(f"--- Child {n + 1} monthly cost: {(child.cost * 30):.2f}$")
            appliances_total = sum(a.cost for a in room.appliances)
            result.append(f"--- Appliances monthly cost: {(appliances_total * 30):.2f}$")

        return "\n".join(result)


    @staticmethod
    def __calculate_cost_for_one_room(room):
        return room.expenses + room.room_cost

    def __remove_rooms(self, rooms):
        for room in rooms:
            self.rooms.remove(room)
