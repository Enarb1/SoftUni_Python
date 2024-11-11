from project.loans.base_loan import BaseLoan


class StudentLoan(BaseLoan):

    LOAN_AMOUNT = 2000.0
    INTEREST_RATE = 1.5
    def __init__(self):
        super().__init__(StudentLoan.INTEREST_RATE, StudentLoan.LOAN_AMOUNT)

    def increase_interest_rate(self):
        self.interest_rate += 0.2