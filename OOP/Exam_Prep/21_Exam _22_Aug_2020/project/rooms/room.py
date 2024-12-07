class Room:
    MONTH = 30
    def __init__(self, name: str, budget: float, members_count: int):
        self.family_name = name
        self.budget = budget
        self.members_count = members_count
        self.children: list = []
        self.__expenses = 0

    @property
    def expenses(self):
        return self.__expenses

    @expenses.setter
    def expenses(self, value):
        if value < 0:
            raise ValueError("Expenses cannot be negative")
        self.__expenses = value

    def calculate_expenses(self, *args):
        total_cost = 0
        for arg in args:
            total_cost += sum(item.cost for item in arg)
        self.expenses = total_cost * self.MONTH