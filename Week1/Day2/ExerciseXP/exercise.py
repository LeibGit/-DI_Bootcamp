
# exercise #1
my_fav_numbers = {18, 8, 12, 400}
my_fav_numbers.add(90)
my_fav_numbers.add(2)
print(my_fav_numbers)
my_fav_numbers.remove(2)

friend_fav_numbers = {45, 70, 88, 5}
our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)
print(our_fav_numbers)


# exercise #2
tuple = (1, 4, 5, 8, 99)
tuple.add(9)
print(tuple)

# exercise #3
basket = ["Banana", "Apples", "Oranges", "Blueberries"]
basket.remove("Banana")
print(basket)
basket.remove("Blueberries")
print(basket)
basket.append("Kiwi")
print(basket)
basket.insert(0, "Apples")
print(basket)
basket.count("Apples")
print(basket)
basket.clear()
print(basket)

# Exercise 4
list_of_nums = []
count = 1
while count < 5:
  count += 0.5
  list_of_nums.append(count)
  print(list_of_nums)

# Exercise 5
for num in range(1, 21):
  print(num)

print(type(str('hello')))

for index, value in enumerate(range(1, 21)):
  if index % 2 == 0:
    print(f"Index: {index}, number: {value}")
  else:
    continue
# Exercise 6
while True: 
  user_name = input("Enter your name: ")
  if user_name.isdigit():
    print("Your name can't be only numbers.")
  elif len(user_name) < 3:
    print("Your name must be at least 3 characters")
  else:
    print("thank you")
    break

# Ecercise 7
list = []
prompt = input("Input your favorite fruit.")
list.append(prompt)
check_fruit = input("Name of fruit: ")
if check_fruit in prompt:
  print("You chose one of your favorite fruits! Enjoy!")
else:
  print("You chose a new fruit. I hope you enjoy it!")


# Exercise 8
all_toppings = []
while True:
  prompt = input("Enter pizza toppings(or enter 'quit' to quit): ").lower()
  
  if prompt == 'quit':
    print(all_toppings)
    price = 10 + (len(all_toppings)* 2.5)
    print(f"Price is ${price}")
    break
  else:
    all_toppings.append(prompt)
    print(prompt)
    print(f"Adding {prompt} to your pizza.")



# Exercise 9
family_members = []
total_cost = 0
while True:
  age = int(input("Add a family members age(enter 'quit' to quit): "))
  if age < 3:
    print("free")
  elif age >= 3 and age <= 12:
    print("10")
    total_cost += 10
  else:
    print('15')
    total_cost += 15
  print(f"cost is equal too: {total_cost}")