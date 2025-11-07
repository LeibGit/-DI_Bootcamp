# Exercise 1
def display_message():
    print("I am learning about functions in python.")
display_message()

# Exercise 2
def favorite_book(title: str):
    print(f"One of my favorite books is {title}")
favorite_book("Alice in Wonderland")


# Exercise 3
def describe_city(city, country='Unknown'):
    print(f"{city} is in {country}")

describe_city("Reykjavik", "Iceland")
describe_city("Paris")

# Exercise 4
from random import randint as r

def random(n):
    if n >= 1 and n <= 100:
       random_num =  r(1, 100)
       if n == random_num:
           print("Success")
    print(f"Fail", f"random num: {random_num}", f"your guess: {n}")
random(20)