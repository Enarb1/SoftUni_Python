from project.client import Client
from project.meals.meal import Meal
from project.meals.dessert import Dessert
from project.meals.main_dish import MainDish
from project.meals.starter import Starter

import copy



class FoodOrdersApp:
    VALID_MEAL_TYPES = ["Starter", "MainDish", "Dessert"]

    def __init__(self):
        self.menu: list = []
        self.clients_list: list = []
        self.receipt_number = 0


    def register_client(self, client_phone_number: str) -> str:
        if self.__get_client(client_phone_number) is not None:
            raise Exception("The client has already been registered!")

        client = Client(client_phone_number)
        self.clients_list.append(client)
        return f"Client {client_phone_number} registered successfully."


    def add_meals_to_menu(self, *meals) -> None:
        for meal in meals:
            if meal.__class__.__name__ in self.VALID_MEAL_TYPES:
                self.menu.append(meal)


    def show_menu(self):
        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")
        return '\n'.join(m.details() for m in self.menu)


    def add_meals_to_shopping_cart(self, client_phone_number: str, **meal_names_and_quantities) -> str:
        client = self.__get_client(client_phone_number)
        shopping_list = {}

        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")
        if client is None:
            self.register_client(client_phone_number)
            client = self.__get_client(client_phone_number)

        for meal in meal_names_and_quantities.keys():
            meal_names = self.__get_meals_by_name(meal)
            if len(meal_names) == 0:
                raise Exception(f"{meal} is not on the menu!")
            meal_name = meal_names[0]
            if meal_names_and_quantities[meal] > meal_name.quantity:
                raise Exception(f"Not enough quantity of {meal_name.__class__.__name__}: {meal_name.name}!")

            shopping_list[meal] = shopping_list.get(meal, 0) + meal_names_and_quantities[meal]
        else:
            self.__add_to_cart(shopping_list, client)
            shopping_cart = ', '.join(m.name for m in client.shopping_cart)
            return f"Client {client_phone_number} successfully ordered {shopping_cart} for {client.bill:.2f}lv."


    def cancel_order(self, client_phone_number: str):
        client = self.__get_client(client_phone_number)
        if len(client.shopping_cart) == 0:
            raise Exception("There are no ordered meals!")
        self.__return_meal_to_menu(client)
        self.__reset_client_cart(client)
        return f"Client {client.phone_number} successfully canceled his order."


    def finish_order(self, client_phone_number: str):
        client = self.__get_client(client_phone_number)
        if len(client.shopping_cart) == 0:
            raise Exception("There are no ordered meals!")
        self.receipt_number += 1
        total = client.bill
        self.__reset_client_cart(client)
        return (f"Receipt #{self.receipt_number} with total amount of {total:.2f} "
                f"was successfully paid for {client.phone_number}.")


    def __str__(self):
        return f"Food Orders App has {len(self.menu)} meals on the menu and {len(self.clients_list)} clients."


    def __reset_client_cart(self, client):
        client.shopping_cart = []
        client.bill = 0.0


    def __return_meal_to_menu(self, client):
        for product in client.shopping_cart:
            for meal in self.menu:
                if product.name == meal.name:
                    meal.quantity += product.quantity


    def __add_to_cart(self, shopping_list: dict, client):

        for m in shopping_list.keys():
            meal = self.__get_meals_by_name(m)[0]
            meal_copy = copy.deepcopy(meal)
            meal.quantity -= shopping_list[m]
            client.bill += meal.price * shopping_list[m]
            client.shopping_cart.append(meal_copy)
            client.shopping_cart[-1].quantity = shopping_list[m]


    def __get_client(self, phone_number: str):
        return next((c for c in self.clients_list if c.phone_number == phone_number), None)


    def __get_meals_by_name(self, name: str) -> list:
        return [m for m in self.menu if m.name == name]

