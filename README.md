# ProgramerimiseAluste_IseseisevToo

See repo sisaldab projecti mis simuleerib panga kontot.

## Funktsionaalsus

### Programm võimaldab:
- luua pangakontosid
- vaadata konto saldot;
- teha sissemakseid;
- võtta raha välja;
- kanda raha ühelt kontolt teisele;
- kontrollida, kas kontol on piisavalt raha;
- kasutada erinevaid kontotüüpe.

### Oodatavada käitumised:

Dave = BankAccount(1000, "Dave")
Sara = BankAccount(1000, "Sara")
Programm loob panga kontod Dave ja Sara

### Kasutaja teeb sissemakse:
Sara.deposit(500)

Tulemus:

Deposit complete.
Account 'Sara' Balance = 1500.00€

### Kasutaja proovib võtta välja rohkem raha, kui kontol on:

Dave.withdraw(10000)

Tulemus:
Withdraw interrupted:
Sorry, account 'Dave' only has balance of 1000.00€

### Raha kantakse ühelt kontolt teisele:
Dave.transfer(100, Sara)

Tulemus:
Transfer complete.

IntrestRewardAccount: Loob konto mis lisab sissemaksele 5% booonuse.
SavingsAccount: Loob konto mis võtab väljamakse teenustasu.


## Mis oskusi demonstreerib

### Klassid ja objektid:

#### Klassid:
BankAccount
InterestRewardAccount
SavingsAccount
BalanceException

Näide:
class BankAccount:
    def __init__(self, initialAmount, accountName):
        self.balance = initialAmount
        self.name = accountName

#### Kapseldamine:
deposit()
withdraw()
transfer()

#### Pärimine:
class InterestRewardAccount(BankAccount):
class SavingsAccount(InterestRewardAccount):

#### olümorphism:
class InterestRewardAccount(BankAccount):
    def deposit(self, amount):

class SavingsAccount(InterestRewardAccount):
    def withdraw(self, amount):

#### Erindite kasutamine:
class BalanceException(Exception):


### Muud oskused:

#### Tingimuslaused:
if self.balance >= amount:

#### Meetodite kasutamine:
getBalance()
deposit()
withdraw()
transfer()
viableTransaction()

#### Veatöötlus:
try:
    self.viableTransaction(amount)
except BalanceException as error:

#### Konstruktorid:
def __init__(self, initialAmount, accountName):