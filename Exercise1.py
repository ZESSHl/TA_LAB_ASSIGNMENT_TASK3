class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance


    @property
    def balance(self):
        return self.__balance


    def _adjust_balance(self, amount):
        self.__balance += amount

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: {amount}")
        else:
            print("Deposit a valid amount")

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"Amount Withdrawn: {amount}")
            return amount
        else:
            print("Insufficient Funds")

    def check_balance(self):
        print(f"Current Balance: {self.__balance}")
        return self.__balance


class SavingsAccount(BankAccount):
    def __init__(self, owner, balance=0.0, annual_rate=0.05):
        super().__init__(owner, balance)
        self.annual_rate = float(annual_rate)

    def apply_monthly_interest(self):
        monthly_rate = self.annual_rate / 12.0
        interest = self.balance * monthly_rate   # use getter property
        self._adjust_balance(interest)           # safely update balance
        print(f"Interest of {interest:.2f} applied.")


if __name__ == "__main__":
    account = BankAccount("Jeff", 1000)
    account.deposit(300)
    account.withdraw(500)
    account.check_balance()

    print("---Savings Account---")
    acct = SavingsAccount("Jeff", 1000, annual_rate=0.06)
    acct.apply_monthly_interest()
    acct.check_balance()

# 1. encapsulation, hiding the balance with __ and letting leaving deposit, withdraw, and check_balance as is
# 2. for security
# 3. refer to line 35 