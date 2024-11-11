from project.loans.student_loan import StudentLoan
from project.loans.mortgage_loan import MortgageLoan
from project.clients.student import Student
from project.clients.adult import Adult


class BankApp:

    VALID_LOAN_TYPES = {
        "StudentLoan": StudentLoan,
        "MortgageLoan": MortgageLoan
    }

    VALID_CLIENT_TYPES = {
        "Student": Student,
        "Adult": Adult
    }

    GRANT_LOAN_TYPES = {
        "Student": "StudentLoan",
        "Adult": "MortgageLoan"
    }

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.loans: list = []
        self.clients: list = []
        self.granted_loans: list = []


    def add_loan(self, loan_type: str):
        try:
            loan = self.VALID_LOAN_TYPES[loan_type]()
        except KeyError:
            raise Exception("Invalid loan type!")

        self.loans.append(loan)

        return f"{loan_type} was successfully added."


    def add_client(self, client_type: str, client_name: str, client_id: str, income: float):
        try:
            client = self.VALID_CLIENT_TYPES[client_type](client_name, client_id, income)
        except KeyError:
            raise Exception("Invalid client type!")

        if len(self.clients) >= self.capacity:
            return "Not enough bank capacity."

        self.clients.append(client)

        return f"{client_type} was successfully added."


    def grant_loan(self, loan_type: str, client_id: str):
        loan = self._get_loan(loan_type)
        client = self._get_client(client_id)

        if loan_type != self.GRANT_LOAN_TYPES[client.__class__.__name__] :
            raise Exception("Inappropriate loan type!")

        client.loans.append(loan)
        self.granted_loans.append(loan)
        self.loans.remove(loan)

        return f"Successfully granted {loan_type} to {client.name} with ID {client_id}."


    def remove_client(self, client_id: str):
        client = self._get_client(client_id)

        if client is None:
            raise Exception("No such client!")

        if client.loans:
            raise Exception("The client has loans! Removal is impossible!")

        self.clients.remove(client)
        return f"Successfully removed {client.name} with ID {client_id}."


    def increase_loan_interest(self, loan_type: str):
        increased_loans = 0
        for loan in self.loans:
            if loan.__class__.__name__ == loan_type:
                increased_loans += 1
                loan.increase_interest_rate()

        return f"Successfully changed {increased_loans} loans."


    def increase_clients_interest(self, min_rate: float):
        increased_interest_rates = 0
        for client in self.clients:
            if client.interest < min_rate:
                increased_interest_rates += 1
                client.increase_clients_interest()

        return f"Number of clients affected: {increased_interest_rates}."


    def get_statistics(self):
        return f"""Active Clients: {len(self.clients)}
Total Income: {self._get_clients_total_income():.2f}
Granted Loans: {len(self.granted_loans)}, Total Sum: {self._get_granted_loans_total_sum():.2f}
Available Loans: {len(self.loans)}, Total Sum: {self._get_not_granted_loans_total_sum():.2f}
Average Client Interest Rate: {self._get_avg_interest_rate():.2f}"""


    def _get_client(self, client_id):
        clients = [c for c in self.clients if c.client_id == client_id]
        return clients[0] if clients else None


    def _get_loan(self, loan_type: str):
        loans = [l for l in self.loans if l.__class__.__name__ == loan_type]
        return loans[0] if loans else None


    def _get_clients_total_income(self):
        return sum([c.income for c in self.clients])


    def _get_granted_loans_total_sum(self):
        return sum([l.amount for l in self.granted_loans])


    def _get_not_granted_loans_total_sum(self):
        return sum([l.amount for l in self.loans])


    def _get_avg_interest_rate(self):
        try:
            avg_interest = sum([c.interest for c in self.clients]) / len(self.clients)
        except ZeroDivisionError:
            return 0

        return avg_interest
