class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, number: int):
        if number <= 0:
            raise ValueError("Enter a number greate than 0.")
        else:
            self.balance += number
            return self
    
    def withdraw(self, number: int):
        if number > self.balance:
            raise ValueError("Number must be less than balance. You can't spend more than you have.")
        elif number <= 0:
            raise ValueError("Enter a number greate than 0.")
        else:
            self.balance -= number
            return self
        
    def __str__(self):
        return f" Balance: {self.balance}"

class MinimumBalanceAccount(BankAccount):
    def __init__(self, balance, minimum_balance=0):
        super().__init__(balance)
        self.minimum_balance = minimum_balance

    def withdraw(self, number: int):
        if self.balance < self.minimum_balance:
            raise ValueError("Balance must be above minimum balance.")
        else:
            return super().withdraw(number)
    

    
if __name__=='__main__':

    joe_account = BankAccount(10000)
    print(joe_account.deposit(600))
    print(joe_account.withdraw(300))
    print(joe_account.balance)

    james_account = MinimumBalanceAccount(50000, 10000)
    print(james_account.deposit(500))
    print(james_account.withdraw(1000))
    print(james_account.balance)