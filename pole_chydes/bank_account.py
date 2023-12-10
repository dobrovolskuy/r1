class BankAccount:
    def __init__(self, name, initial_balance=0):
        self.name = name
        self.balance = initial_balance

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount} UAH. Current balance: {self.balance} UAH.")
        else:
            print("Insufficient funds or invalid withdrawal amount.")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount} UAH. Current balance: {self.balance} UAH.")
        else:
            print("Invalid deposit amount.")

    def __str__(self):
        return f"Account {self.name}: {self.balance} UAH."


account = BankAccount(name="Primary Account", initial_balance=1000)


account.withdraw(500)
account.deposit(200)


print(account)