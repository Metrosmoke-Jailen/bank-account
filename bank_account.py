import random

class BankAccount:
    def __init__(self, full_name, account_number=None, balance=0):
        self.full_name = full_name

        if account_number:
            self.account_number = str(account_number).zfill(8)
        else:
            self.account_number = str(random.randint(10000000, 99999999))

        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Amount deposited: ${amount:.2f} new balance: ${self.balance:.2f}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
            self.balance -= 10
            print("Overdraft fee: $10.00 charged.")
            print(f"New balance: ${self.balance:.2f}")
        else:
            self.balance -= amount
            print(f"Amount withdrawn: ${amount:.2f} new balance: ${self.balance:.2f}")

    def get_balance(self):
        print(f"Current balance: ${self.balance:.2f}")
        return self.balance

    def add_interest(self):
        interest = self.balance * 0.00083
        self.balance += interest
        print(f"Interest added: ${interest:.2f} new balance: ${self.balance:.2f}")

    def print_statement(self):
        print(self.full_name)
        print(f"Account No.: ****{self.account_number[-4:]}")
        print(f"Balance: ${self.balance:.2f}")
        print("-" * 30)

mitchell = BankAccount("Mitchell", account_number="03141592")
mitchell.deposit(400000)
mitchell.print_statement()
mitchell.add_interest()
mitchell.print_statement()
mitchell.withdraw(150)
mitchell.print_statement()