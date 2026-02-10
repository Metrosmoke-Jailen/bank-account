import random

class BankAccount:
    def __init__(self, full_name, account_number=None, balance=0):
        self.full_name = full_name

        # Allow manual account number OR generate random 8-digit number
        if account_number:
            self.account_number = str(account_number).zfill(8)
        else:
            self.account_number = str(random.randint(10000000, 99999999))

        self.balance = balance
