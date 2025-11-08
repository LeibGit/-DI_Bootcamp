# Exercise 1
def insert_item(index, item):
    random_list = [1, 4, 'hello', 78, '12']
    random_list.insert(index, item)
    print(random_list)
insert_item(3, 'hello')

# Exercise 2
def count_spaces(text: str):
    print(text.count(' '))
count_spaces('hell    o')

# Exercise 3
def get_upper(text: str):
    lowercase = 0
    uppercase = 0
    for char in text:
        if char.isupper():
            uppercase += 1
        else:
            lowercase += 1
    print(f"Uppercase: {uppercase} | Lowercase: {lowercase}")
get_upper('HeLlO')

# Exercise 4
def find_sum(lst: list):
    total = 0
    for num in lst:
        total = total + num
    print(total)
find_sum([1, 4, 5])

# Exercise 5
def get_max(nums: list):
    print(max(nums))
get_max([1, 5, 58, 90])

# Exercise 6
def factorial(n: int):
    total = 1
    if n < 0:
        print("Need positive num.")
    else:
        for i in range(1, n+1):
            total *= i
    print(total)
factorial(12)

# Exercise 6
def counter(items: list, letter: str):
    count = 0
    stringify = ''.join(items)
    for char in stringify:
        if char == letter:
            count += 1
    print(count)
counter(['a','a','t','o'], 'a')

from math import sqrt

def norm(nums: list):
    squares = []
    for n in nums:
        squares.append(n**2)
    l2_norm = sqrt(sum(squares))
    print(l2_norm)
norm([1, 2, 2])

def is_monotonic(nums: list):
    for index, num in enumerate(nums):
        if num[index] < num[index + 1]:
            print('ascending')
            return True
        elif num[index] > num[index + 1]:
            print('decending')
            return True
        else:
            return False
is_monotonic([7,6,5,5,2,0])