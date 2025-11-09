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


def longest_word(words: list):
    length = []
    for word in words:
        length.append(len(word))
    index_max_str =  length.index(max(length)) 
    print(words[index_max_str])
longest_word(['hello', 'jello', 'spy', 'coding'])

def seperate(items: list):
    strings = []
    nums = []
    for item in items:
        if type(item) == int:
            nums.append(item)
        else:
            strings.append(item)
    print(strings)
    print(nums)
seperate([1, 'hello', 12, 'spy', 56, 'code'])

def is_palindrome(text: str):
    if text == text[::-1]:
        print("is palindrome")
    else:
        print("Not palindrome")
is_palindrome('john')
is_palindrome('radar')

def sum_over_k(sentence: str, k: int):
    greater_than = []
    words = sentence.split()
    for word in words:
        if len(word) > k:
            greater_than.append(word)
    print(greater_than)
sum_over_k(sentence='Do or do not there is no try', k=3)

def average(items: dict):
    lst_of_values = []
    total = 0
    for value in items.values():
        lst_of_values.append(value)
        total += value
    
    avg = total / len(lst_of_values)
    print(avg)
average({'a': 1,'b':2,'c':8,'d': 1})

def common_div(n1, n2):
    list_of_div = []
    get_min =  min(n1, n2)
    numbers = list(range(2, get_min + 1))
    print(numbers)
    for n in numbers:
        if n1 % n == 0 and n2 % n == 0:
            list_of_div.append(n)
    print(list_of_div)
common_div(10, 20)

def weird_print(lst: list):
    for index, value in enumerate(lst):
        if value % 2 == 0:
            print(f"{index}: {value}")
weird_print([1,2,2,3,4,5])
