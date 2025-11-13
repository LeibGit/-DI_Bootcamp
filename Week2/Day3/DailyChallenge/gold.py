count = 0

lst_of_users = []

while count < 5:

    name = input("Enter a name: ")
    age = int(input("Enter an age: "))
    score = int(input("Enter a score: "))
    lst_of_users.append((name, age, score))
    count += 1
lst_of_users.sort(key=lambda x: (x[0], x[1], x[2]))
print(lst_of_users)