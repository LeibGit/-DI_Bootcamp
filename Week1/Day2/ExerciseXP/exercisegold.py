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
