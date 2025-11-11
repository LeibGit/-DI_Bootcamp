class BankAccount:
    def __init__(self, balance, username, password, authenticated=False):
        self.balance = balance
        self.username = username
        self.password = password
        self.authenticated = authenticated

    def deposit(self, number: int):
        if self.authenticated:
            if number <= 0:
                raise ValueError("Enter a number greater than 0.")
            self.balance += number
            return self
        else:
            raise UserWarning("You are not authenticated to do this.")
    
    def withdraw(self, number: int):
        if self.authenticated:
            if number > self.balance:
                raise ValueError("Number must be less than balance.")
            elif number <= 0:
                raise ValueError("Enter a number greater than 0.")
            self.balance -= number
            return self
        else:
            raise UserWarning("You are not authenticated to do this.")
    
    def authenticate(self, username, password):
        if username == self.username and password == self.password:
            self.authenticated = True
            return self
        else:
            raise ValueError("Not a user.")

    def __str__(self):
        return f"Balance: {self.balance}"


class MinimumBalanceAccount(BankAccount):
    def __init__(self, balance, username, password, minimum_balance=0):
        super().__init__(balance, username, password)
        self.minimum_balance = minimum_balance

    def withdraw(self, number: int):
        if self.balance - number < self.minimum_balance:
            raise ValueError("Withdrawal would drop below minimum balance.")
        return super().withdraw(number)


class ATM:
    def __init__(self, account_list: list, try_limit: int):
        if not isinstance(account_list, list):
            raise ValueError("account must be a list")
        for acc in account_list:
            if not isinstance(acc, (BankAccount, MinimumBalanceAccount)):
                raise ValueError("Must be a type of bank account")
            
        if not isinstance(try_limit, int) or try_limit <= 0:
            raise ValueError("Must be a number above 0.")
        
        self.account_list = account_list
        self.try_limit = try_limit
        self.current_tries = 0
    
    def log_in(self, username, password):
        for acc in self.account_list:
            try:
                acc.authenticate(username, password)
                print(f"Login successful! Welcome, {acc.username}.")
                self.current_tries = 0
                return self.show_account_menu(acc)
            except ValueError:
                continue

        self.current_tries += 1
        if self.current_tries >= self.try_limit:
            raise StopIteration("Max tries reached!")
        else:
            print("Invalid credentials, try again.")

    def show_account_menu(self, account):
        while True:
            user_selection = input("Type: deposit, withdraw, or exit: ").lower()
            if user_selection == "exit":
                account.authenticated = False
                print("Logged out.")
                break
            elif user_selection == "deposit":
                try:
                    amount = float(input("Enter amount: "))
                    account.deposit(amount)
                    print(f"Deposit successful. New balance: {account.balance}")
                except Exception as e:
                    print(e)
            elif user_selection == "withdraw":
                try:
                    amount = float(input("How much would you like to withdraw: "))
                    account.withdraw(amount)
                    print(f"Withdrawal successful. New balance: {account.balance}")
                except Exception as e:
                    print(e)
            else:
                print("Invalid input.")


if __name__=='__main__':
    joe = BankAccount(1000, "joe", "1234")
    jane = MinimumBalanceAccount(5000, "jane", "abcd", minimum_balance=500)
    atm = ATM([joe, jane], try_limit=3)
    atm.log_in("joe", "1234")
