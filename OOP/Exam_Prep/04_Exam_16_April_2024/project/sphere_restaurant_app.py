from project.waiters.full_time_waiter import FullTimeWaiter
from project.waiters.half_time_waiter import HalfTimeWaiter
from project.clients.regular_client import RegularClient
from project.clients.vip_client import VIPClient



class SphereRestaurantApp:

    VALID_WAITER_TYPES = {
        "FullTimeWaiter": FullTimeWaiter,
        "HalfTimeWaiter": HalfTimeWaiter,
    }

    VALID_CLIENT_TYPES = {
        "RegularClient":RegularClient,
        "VIPClient": VIPClient
    }

    def __init__(self):
        self.waiters: list = []
        self.clients: list = []

    def hire_waiter(self,waiter_type: str, waiter_name: str, hours_worked: int):

        try:
            waiter = self.VALID_WAITER_TYPES[waiter_type](waiter_name, hours_worked)
        except KeyError:
            return f"{waiter_type} is not a recognized waiter type."

        try:
            search_waiters = next(filter(lambda w: w.name == waiter_name, self.waiters))
            return f"{waiter_name} is already on the staff."
        except StopIteration:

            self.waiters.append(waiter)

            return f"{waiter_name} is successfully hired as a {waiter_type}."


    def admit_client(self, client_type: str, client_name: str):
        try:
            client = self.VALID_CLIENT_TYPES[client_type](client_name)
        except KeyError:
            return f"{client_type} is not a recognized client type."

        try:
            search_clients = next(filter(lambda c: c.name == client_name, self.clients))
            return f"{client_name} is already a client."
        except StopIteration:

            self.clients.append(client)
            return f"{client_name} is successfully admitted as a {client_type}."


    def process_shifts(self, waiter_name: str):
        try:
            waiter = next(filter(lambda w: w.name == waiter_name, self.waiters))
            return waiter.report_shift()
        except StopIteration:
            return f"No waiter found with the name {waiter_name}."


    def process_client_order(self, client_name: str, order_amount: float):
        try:
            client = next(filter(lambda c: c.name == client_name, self.clients))
            return f"{client_name} earned {client.earning_points(order_amount)} points from the order."
        except StopIteration:
            return f"{client_name} is not a registered client."


    def apply_discount_to_client(self, client_name: str):
        try:
            client = next(filter(lambda c: c.name == client_name, self.clients))
        except StopIteration:
            return f"{client_name} cannot get a discount because this client is not admitted!"

        discount, points = client.apply_discount()
        return f"{client_name} received a {discount}% discount. Remaining points {points}"

    def sort_waiters(self):
        return sorted(self.waiters, key=lambda w: w.calculate_earnings(), reverse=True)


    def total_earnings(self):
        return sum(w.calculate_earnings() for w in self.waiters)


    def total_client_points(self):
        return sum(c.points for c in self.clients)

    def waiter_details(self):
        waiter_details = '\n'.join(str(w) for w in self.sort_waiters())
        return f"** Waiter Details **\n{waiter_details}" if waiter_details else "** Waiter Details **"


    def generate_report(self):
        return (f"$$ Monthly Report $$\n"
                f"Total Earnings: ${self.total_earnings():.2f}\n"
                f"Total Clients Unused Points: {self.total_client_points()}\n"
                f"Total Clients Count: {len(self.clients)}\n"
                f"{self.waiter_details()}")
