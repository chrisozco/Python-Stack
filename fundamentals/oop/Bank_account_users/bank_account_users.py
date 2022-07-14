class BankAccount:
    bank_name = "Dojo Bank"

    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if (self.balance - amount) >= 0:
            self.balance -= amount
        else:
            print("Insuficient Funds: $5 fee charged")
            self.balance -= 5
        return self

    def display_account_info(self):
        return self.balance

    def yield_interest(self):
        if self.balance > 0:
            self.balance += (self.balance * self.int_rate)
        return self

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = {
            "checking": BankAccount(0.02, 0),
            "savings": BankAccount(0.10, 3000)
        }

    def display_user_balance(self):
        print(F"User: {self.name}, Checking: {self.account['checking'].display_account_info()}")
        print(F"User: {self.name}, Saving: {self.account['savings'].display_account_info()}")
        return self


chris = User("Chris", "chris@dojobank.com")

chris.account['checking'].deposit(200)
chris.account['savings'].deposit(2000)
chris.display_user_balance()






# account_01 = BankAccount(0.02, 30000)
# account_02 = BankAccount(0.067, 5500)

# account_01.display_account_info().deposit(200).deposit(250).deposit(4350).withdraw(1500).display_account_info()

# account_02.display_account_info().deposit(20).deposit(200).withdraw(3500).withdraw(1230).withdraw(275).withdraw(1000).display_account_info()
