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
    
if __name__=='__main__':

    joe_account = BankAccount(10000)
    print(joe_account.deposit(600))
    print(joe_account.withdraw(300))
    print(joe_account.balance)