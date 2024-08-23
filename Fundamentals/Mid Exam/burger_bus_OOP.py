class BurgerBus:
    __visited_cities = 0

    def __init__(self, city, income, expenses):
        self.city = city
        self.income = income
        self.expenses = expenses
        self.profit = self.income - self.expenses
        BurgerBus.__visited_cities += 1

    def revenue(self):
        if self.__visited_cities % 3 == 0:
            if self.__visited_cities % 5 == 0:
                pass
            else:
                self.profit -= 0.5 * self.expenses
            if self.__visited_cities % 5 == 0:
                self.profit -= 0.1 * self.income


    def __repr__(self):
        return f"In {self.city} Burger Bus earned {self.profit:.2f} leva."



number_of_cities = int(input())
total_profit = 0
while number_of_cities > 0:
    city = input()
    income = float(input())
    expenses = float(input())
    bus = BurgerBus(city, income, expenses)
    bus.revenue()
    total_profit += bus.profit
    print(bus)
    number_of_cities -= 1

print(f"Burger Bus total profit: {total_profit:.2f} leva.")