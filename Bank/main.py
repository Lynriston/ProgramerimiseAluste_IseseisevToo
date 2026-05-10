"""Bank."""


class BalanceException(Exception):
    """BalanceException exeption class."""
    pass


class BankAccount:
    """Bank account class."""
    def __init__(self, initialAmount, accountName):
        """Bank Account class initialization."""
        self.balance = initialAmount
        self.name = accountName
        print(f"\nAccount '{self.name}' created. \nBalance = {self.balance:.2f}€")

    def getBalance(self):
        """Show balance of account."""
        print(f"\nAccount '{self.name}' Balance = {self.balance:.2f}€")

    def deposit(self, amount):
        """Deposite currency into account."""
        self.balance = self.balance + amount
        print("\nDeposit complete.")
        self.getBalance()

    def viableTransaction(self, amount):
        """Check if account has the necessary amount of income."""
        if self.balance >= amount:
            return
        else:
            raise BalanceException(f"\nSorry, account '{self.name}' only has balance of {self.balance:.2f}€")
        
    def withdraw(self, amount):
        """Withdraw currency from account if possible."""
        try:
            self.viableTransaction(amount)
            self.balance = self.balance - amount
            print("\nWithdraw complete.")
            self.getBalance()
        except BalanceException as error:
            print(f'\nWithdraw interrupted: {error}')

    def transfer(self, amount, account):
        """Transfer currency from one account to another account if possible."""
        try:
            print("\n**********\n\nBeggining Transfer...")
            self.viableTransaction(amount)
            self.withdraw(amount)
            account.deposit(amount)
            print("\nTransfer complete!\n\n**********")
        except BalanceException as errot:
            print(f"\nTransfer interrupted!")


class IntrestRewardAccount(BankAccount):
    """Intrest Reward Account class."""
    def deposit(self, amount):
        """Deposit currency into Intrest Reward Account."""
        self.balance = self.balance + (amount * 1.05)
        print("\nDeposit complete.")
        self.getBalance()


class SavingsAccount(IntrestRewardAccount):
    """Savings Account class."""
    def __init__(self, initialAmount, accountName):
        """Savings Account sub-class initialization."""
        super().__init__(initialAmount, accountName)
        self.fee = 5

    def withdraw(self, amount):
        """Withdraw from Savings account if possible."""
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