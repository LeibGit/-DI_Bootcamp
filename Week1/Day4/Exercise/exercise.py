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
from random import randint, uniform

def random(n):
    if n >= 1 and n <= 100:
       random_num =  randint(1, 100)
       if n == random_num:
           print("Success")
    print(f"Fail", f"random num: {random_num}", f"your guess: {n}")
random(20)

# Exercise 5
def make_shirt(size="large", text="I love python"):
    print(f"your shirt size is {size}. The shirt says {text}")
make_shirt()
make_shirt(size="medium")
make_shirt(size="small", text="I love javascript")

# Exercise 6
magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']
def show_magicians():
    for name in magician_names:
        print(name)
show_magicians()

def make_great(magician_names):
    for name in magician_names:
        print(f"The great {name}")
make_great(magician_names=magician_names)

# Exercise 7
def get_random_temp():
    user_input = int(input("Enter a month 1-12: "))
    if user_input == 12 or user_input == 1 or user_input == 2:
        return 'Winter'
    elif user_input >= 3 and user_input <=5:
        return 'Spring'
    elif user_input >= 6 and user_input <= 8:
        return 'Summer'
    else:
        return 'Autumn'
def main():
    season = get_random_temp()
    print(f"The season is {season}.")
    if season == 'Winter':
        print("Brrr, that’s freezing! Wear some extra layers today.")
    elif season == 'Spring':
        print("A bit warm, stay hydrated.")
    elif season == 'Summer':
        print("It’s really hot! Stay cool.")
    elif season == 'Autumn':
        print("Quite chilly! Don’t forget your coat.")
main()