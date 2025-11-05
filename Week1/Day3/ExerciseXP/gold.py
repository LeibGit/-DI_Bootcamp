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