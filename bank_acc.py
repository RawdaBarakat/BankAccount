class bank_exception(Exception):
    pass

class BankAccount:
    def __init__(self , acc_name , acc_balance):
        self.name = acc_name
        self.balance = acc_balance

    def deposite(self,amount):
        self.balance += amount
        print("the deposite process accomplished successfully ")
        self.get_balance()

    def get_balance(self):
        print(f"your current balance is : {self.balance}")

    def viable_transaction(self , amount):
        if self.balance >= amount :
            return
        else :
            raise bank_exception(f"sorry this process can`t complete , your balance only :{self.balance}")

    def withdraw(self, amount):
        try:
            self.viable_transaction(amount)
            self.balance -= amount
            print("the withdraw process accomplished successfully ")
            self.get_balance()
        except BaseException as error :
            print(f"withdraw interrupted {error}")

    def transfer(self , account , amount):
        try:
            print('\n*********************************************************\n\nBeginning Transfer.. 🚀')
            self.viable_transaction(amount)
            self.withdraw(amount)
            account.deposite(amount)
            print('\nTransfer complete! ✅\n\n*********************************************************')
        except BaseException as error:
            print(f"transfer interrupted {error}")

class RewardsAcct(BankAccount):
    def deposite(self,amount):
        self.balance = self.balance + (amount * 1.05)
        print("the deposite process accomplished successfully ")
        self.get_balance()

class SavingsAcct(RewardsAcct):
    def __init__(self, name, balance):
        super().__init__(name, balance)
        self.fee = 5

    def withdraw(self, amount):
        try:
            self.viable_transaction(amount + self.fee)
            self.balance = self.balance - (amount + self.fee)
            print("\nWithdraw completed.")
            self.get_balance()
        except BaseException as error:
            print(f'\nWithdraw interrupted: {error}')
