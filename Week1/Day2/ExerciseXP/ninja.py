# Exercise 1
import math

C=50
H=30
nums = input("Give a comma seperated list of numbers: ").split(',')

for D in nums:
  D = int(D)
  Q = math.sqrt((2 * C * D)/H)
  print(Q)

# Exercise 2
list_of_ints = [3, 47, 99, -80, 22, 97, 54, -23, 5, 7] 
print(list_of_ints)
print(sorted(list_of_ints))
print(sum(list_of_ints))
max_num = max(list_of_ints)
min_num = min(list_of_ints)
print([min_num, max_num])

new_list = []
for n in list_of_ints:
  if n > 50:
    new_list.append(n)
print(new_list)