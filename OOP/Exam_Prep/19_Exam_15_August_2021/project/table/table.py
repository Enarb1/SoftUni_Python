from abc import ABC

from project.baked_food.baked_food import BakedFood
from project.drink.drink import Drink


class Table(ABC):
    def __init__(self, table_number: int, capacity: int):
        self.table_number = table_number
        self.capacity = capacity
        self.food_orders: list = []
        self.drink_orders: list = []
        self.number_of_people: int = 0
        self.is_reserved: bool = False

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, value):
        if not value > 0:
            raise ValueError("Capacity has to be greater than 0!")
        self.__capacity = value

    def reserve(self, number_of_people: int):
        self.number_of_people = number_of_people
        self.is_reserved = True

    def order_food(self, baked_food: BakedFood):
        self.food_orders.append(baked_food)

    def order_drink(self, drink: Drink):
        self.drink_orders.append(drink)

    def get_bill(self):
        food = sum([f.price for f in self.food_orders])
        drinks = sum([d.price for d in self.drink_orders])
        total_bill = food + drinks
        return total_bill

    def clear(self):
        self.food_orders = []
        self.drink_orders = []
        self.number_of_people = 0
        self.is_reserved = False

    def free_table_info(self):
        if not self.is_reserved:
            return (
                f"Table: {self.table_number}\n"
                f"Type: {self.__class__.__name__}\n"
                f"Capacity: {self.capacity}"
            )
