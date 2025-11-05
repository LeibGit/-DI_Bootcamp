"""
# Exercise #1
birthdays = {
    "John": "2020/10/03",
    "James": "1990/01/03",
    "Marry": "2000/04/20",
    "Rob": "2004/07/13", 
    "Greg": "1998/11/05"
}

for user, birthday in birthdays.items():
    print(f"welcome {user} your birthday is {birthday}. You can look up other birthdays of the peoeple in the list!")

    req = input("Give me a name to return a birthday(or press 'q' to quit): ")
    if req in birthdays.keys():
        print(f"Birthday is: {birthdays[req]}")
    elif req == 'q':
        break
    else:
        print("Name not in directory. Try again!")
        continue
# Exercise 2
for key, value in birthdays.items():
    print(f"{key}: {value}")
user_input = input("Enter a name in the directory: ")
if user_input in birthdays.keys():
    print(f"{user_input}'s birthday is {birthdays[user_input]}")
else:
    print(f"Sorry, we don't have the birthday information for {user_input}.")

# Exercise 3
prompt_name = input("what is your name: ")
prompt_birthday = input("What is your birthday: ")
birthdays[prompt_name] = prompt_birthday
new_input = input("Enter a name in the directory: ")
if new_input in birthdays.keys():
     print(f"{new_input}'s birthday is {birthdays[new_input]}")
else:
    print(f"Sorry, we don't have the birthday information for {new_input}.")

# Exercise 4
items = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

for item, price, stock in items.items():
    print(f"Item: {item}, Price: {price}, stock: {stock}")

"""
items = {
    "banana": {"price": 4 , "stock":10},
    "apple": {"price": 2, "stock":5},
    "orange": {"price": 1.5 , "stock":24},
    "pear": {"price": 3 , "stock":1}
}

cost = 0
for fruit, data in items.items():
    total_cost = data["price"] * data["stock"]
    cost += total_cost
print(cost)