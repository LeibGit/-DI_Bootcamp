# Exercise 1
list1 = [1, 2, 6, 7]
list2 = [8, 20, 79]

new_list = list(set(list1).union(set(list2)))
print(new_list)

# Exercise 2
for i in range(1500, 2500):
  if i % 5 == 0:
    print(i)
  elif i % 7 == 0:
    print(i)
  else:
    continue

# Exercise 3
names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']
prompt = str(input("What is your name: "))
if prompt in names:
  print(f"Your name is already in the list {prompt}.")

# Exercise 4
count = 0
list_of_nums = []
while count < 3:
  prompt = int(input("Enter a number: "))
  list_of_nums.append(prompt)
  count += 1

maxim = max(list_of_nums)
print(f"The greatest number is {maxim}")

# Exercise 5
import string
lowercase_alphabet = string.ascii_lowercase
print(lowercase_alphabet)
vowels = ['a', 'e', 'i', 'o', 'u']
for char in lowercase_alphabet:
  if char in vowels:
    print("Vowel")
  else:
    print("constant")

# Exercise 6
word_list = list(input("Enter 7 different words: "))
letter = str(input("Enter in a character: "))

for index, word in enumerate(word_list):
  if letter in word:
    print(index)
  else:
    print(f"{letter} was not in any of the word in your list.")


# exercise 7
list = list(range(1, 1000001))
list_min = min(list)
list_max = max(list)
list_sum = sum(list)
print(list_min)
print(list_max)
print(list_sum)


# Exercise 8
prompt = input("Enter a list of nums seperated by comma: ").split(',')
list1 = list(prompt)
tuple1 = tuple(prompt)
print(list1)
print(tuple1)



# Exercise 9
import random

games_won = 0
games_lost = 0

while True:
  prompt = input("Enter a number between 1 and 9 (press q to quit): ")
  random_num = random.randint(1, 9)
  print(random_num)

  if prompt == random_num:
    print("Winner")
    games_won += 1
  elif prompt == 'q':
    break
  else:
    print("Better luck next time.")
    games_lost += 1
print(f"Games Won: {games_won}")
print(f"Games Lost: {games_lost}")