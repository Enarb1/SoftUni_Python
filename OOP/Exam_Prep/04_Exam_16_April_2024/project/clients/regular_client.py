from project.clients.base_client import BaseClient


class RegularClient(BaseClient):

    def __init__(self, name: str):
        super().__init__(name, "Regular")

    def earning_points(self, order_amount: float):
        points = int(order_amount / 10)
        self.points += points

        return points

