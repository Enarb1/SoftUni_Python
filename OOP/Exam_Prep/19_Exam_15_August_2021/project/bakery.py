from project.baked_food.bread import Bread
from project.baked_food.cake import Cake
from project.drink.tea import Tea
from project.drink.water import Water
from project.table.inside_table import InsideTable
from project.table.outside_table import OutsideTable


class Bakery:
    VALID_FOOD_TYPES = {
        "Bread": Bread,
        "Cake": Cake
    }

    VALID_DRINK_TYPES = {
        "Tea": Tea,
        "Water": Water
    }

    VALID_TABLE_TYPES = {
        "InsideTable": InsideTable,
        "OutsideTable": OutsideTable
    }

    def __init__(self, name: str):
        self.name = name
        self.food_menu: list = []
        self.drinks_menu: list = []
        self.tables_repository: list = []
        self.total_income = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value.strip():
            raise ValueError("Name cannot be empty string or white space!")
        self.__name = value

    def add_food (self, food_type: str, name: str, price: float):
        if self.__get_food_by_name(name) is not None:
            raise Exception(f"{food_type} {name} is already in the menu!")
        if food_type in self.VALID_FOOD_TYPES.keys():
            food = self.VALID_FOOD_TYPES[food_type](name, price)
            self.food_menu.append(food)
            return f"Added {food.name} ({food.__class__.__name__}) to the food menu"

    def add_drink (self, drink_type: str, name: str, portion: float, brand:str):
        if self.__get_drink_by_name(name) is not None:
            raise Exception(f"{drink_type} {name} is already in the menu!")
        if drink_type in self.VALID_DRINK_TYPES.keys():
            drink = self.VALID_DRINK_TYPES[drink_type](name, portion, brand)
            self.drinks_menu.append(drink)
            return f"Added {drink.name} ({drink.brand}) to the drink menu"

    def add_table (self, table_type: str, table_number: int, capacity: int):
        if self.__get_table_by_number(table_number) is not None:
            raise Exception(f"Table {table_number} is already in the bakery!")
        if table_type in self.VALID_TABLE_TYPES.keys():
            table = self.VALID_TABLE_TYPES[table_type](table_number, capacity)
            self.tables_repository.append(table)
            return f"Added table number {table.table_number} in the bakery"

    def reserve_table (self, number_of_people: int):
        table = next((t for t in self.tables_repository if not t.is_reserved and t.capacity >= number_of_people), None)
        if table is not None:
            table.reserve(number_of_people)
            return f"Table {table.table_number} has been reserved for {number_of_people} people"

        return f"No available table for {number_of_people} people"

    def order_food (self, table_number: int, *food_names):
        table = self.__get_table_by_number(table_number)
        if table is None:
            return f"Could not find table {table_number}"

        available_food = []
        unavailable_food = []
        for food_name in food_names:
            food = self.__get_food_by_name(food_name)
            if food is not None:
                available_food.append(food)
                table.order_food(food)
            else:
                unavailable_food.append(food_name)
        result = self.__print_order_result(available_food, unavailable_food, table.table_number)
        return result

    def order_drink (self, table_number: int, *drinks_names):
        table = self.__get_table_by_number(table_number)
        if table is None:
            return f"Could not find table {table_number}"

        available_drink = []
        unavailable_drink = []
        for drink_name in drinks_names:
            drink = self.__get_drink_by_name(drink_name)
            if drink is not None:
                available_drink.append(drink)
                table.order_drink(drink)
            else:
                unavailable_drink.append(drink_name)
        result = self.__print_order_result(available_drink, unavailable_drink, table.table_number)
        return result

    def leave_table (self, table_number: int):
        table = self.__get_table_by_number(table_number)
        if table is not None:
            bill = table.get_bill()
            self.total_income += bill
            table.clear()
            return f"Table: {table.table_number}\nBill: {bill:.2f}"

    def get_free_tables_info(self):
        result = [t.free_table_info() for t in self.tables_repository if not t.is_reserved]
        if result:
            return "\n".join(result)

    def get_total_income(self):
        return f"Total income: {self.total_income:.2f}lv"

    def __print_order_result(self, available, unavailable, table_number):
        result = [f"Table {table_number} ordered:"]
        for p in available:
            result.append(p.__repr__())

        result.append(f"{self.name} does not have in the menu:")
        for p in unavailable:
            result.append(p)

        return "\n".join(result)

    def __get_table_by_number(self, number):
        return next((t for t in self.tables_repository if t.table_number == number), None)

    def __get_drink_by_name(self, name):
        return next((d for d in self.drinks_menu if d.name == name), None)

    def __get_food_by_name(self, name):
        return next((f for f in self.food_menu if f.name == name), None)
