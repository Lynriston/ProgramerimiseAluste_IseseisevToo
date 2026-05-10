"""Bank."""


class BalanceException(Exception):
    pass


class BankAccount:
    def __init__(self, initialAmount, accountName):
        """Bank Account class."""
        self.balance = initialAmount
        self.name = accountName
        print(f"\nAccount '{self.name}' created. \nBalance = {self.balance:.2f}€")

    def getBalance(self):
        print(f"\nAccount '{self.name}' Balance = {self.balance:.2f}€")

    def deposit(self, amount):
        self.balance = self.balance + amount
        print("\nDeposit complete.")
        self.getBalance()

    def viableTransaction(self, amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceException(f"\nSorry, account '{self.name}' only has balance of {self.balance:.2f}€")
        
    def withdraw(self, amount):
        try:
            self.viableTransaction(amount)
            self.balance = self.balance - amount
            print("\nWithdraw complete.")
            self.getBalance()
        except BalanceException as error:
            print(f'\nWithdraw interrupted: {error}')

    def transfer(self, amount, account):
        try:
            print("\n**********\n\nBeggining Transfer...")
            self.viableTransaction(amount)
            self.withdraw(amount)
            account.deposit(amount)
            print("\nTransfer complete!\n\n**********")
        except BalanceException as errot:
            print(f"\nTransfer interrupted!")


class IntrestRewardAccount(BankAccount):
    def deposit(self, amount):
        self.balance = self.balance + (amount * 1.05)
        print("\nDeposit complete.")
        self.getBalance()


class SavingsAccount(IntrestRewardAccount):
    def __init__(self, initialAmount, accountName):
        super().__init__(initialAmount, accountName)
        self.fee = 5

    def withdraw(self, amount):
        try:
            self.viableTransaction(amount + self.fee)
            self.balance = self.balance - (amount + self.fee)
            print("\nWithdraw complete.")
            self.getBalance()
        except BalanceException as error:
            print(f"\nWitdraw interrupted: {error}")


if __name__ == '__main__':
    Dave = BankAccount(1000, "Dave")
    Sara = BankAccount(1000, "Sara")

    Dave.getBalance()
    Sara.getBalance()

    Sara.deposit(500)
    Dave.withdraw(10000)
    Dave.withdraw(100)
    
    Dave.transfer(10000, Sara)
    Dave.transfer(100, Sara)

    Jim = IntrestRewardAccount(1000, "Jim")

    Jim.getBalance()

    Jim.deposit(100)

    Jim.transfer(100, Dave)

    Blaze = SavingsAccount(1000, "Blaze")
    Blaze.getBalance()
    Blaze.deposit(100)
    Blaze.transfer(10000, Sara)