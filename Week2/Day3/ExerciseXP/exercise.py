# Exercise 1

class Currency:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount
        
    def __str__(self):
        return f"{self.amount} dollars."
    
    def __int__(self):
        return int(self.amount)
    
    def __repr__(self):
        return f"{self.amount} dollars."
    
    def __add__(self, other):

        if isinstance(other, Currency):
            if self.currency == other.currency:
                return self.amount + other.amount
            else:
                raise ValueError("Must be same currency")
        elif type(other) == int:
            return self.amount + other
        else:
            raise ValueError("Must be an instance of a currency")
    
    def __iadd__(self, other):
        if isinstance(other, Currency):
            self.amount += other.amount
            return self
        elif type(other) == int:
            self.amount += other
            return self
        else:
            raise ValueError("Must be an instance of a currency")
        
# Exercise 2
from func import sum_of_nums

# Exercise 3
import string
import random

upper_alphabet = string.ascii_uppercase

new_str = ''
for i in range(0, 5):
    rand = random.choice(upper_alphabet)
    new_str += rand

# Exercise 4

from datetime import datetime, date

current_time= datetime.now()
current_date = current_time.date()

# Exercise 5

january_first = date(2025, 1, 1)
print(january_first)

def time_till():
    return current_date - january_first

# Exercise 6
birthday = date(2004, 10, 12)
def time_alive():
    delta = current_date - birthday
    total_minutes = delta.total_seconds() / 60
    return total_minutes

# Exercise 7
from faker import Faker

fake = Faker()
users = []

def add_users(users_to_generate):
    for user in range(users_to_generate):
        user_dict = {"name": fake.name(), "address": fake.address(), "language_code": fake.language_code()}
        users.append(user_dict)
    return users



if __name__=="__main__":
    sum_of_nums(12, 5)
    print(new_str)
    print(current_date)
    print(time_till())
    print(time_alive())
    print(add_users(12))