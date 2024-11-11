from project.loans.base_loan import BaseLoan


class MortgageLoan(BaseLoan):
    LOAN_AMOUNT = 50_000.0
    INTEREST_RATE = 3.5

    def __init__(self):
        super().__init__(MortgageLoan.INTEREST_RATE,MortgageLoan.LOAN_AMOUNT)


    def increase_interest_rate(self):
        self.interest_rate += 0.5