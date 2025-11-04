# Exercise 1
import math
import string

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

def greater_than():
  new_list = []
  for n in list_of_ints:
    if n > 50:
      new_list.append(n)
  print(new_list)
greater_than()

def less_than():
  new_list = []
  for n in list_of_ints:
    if n < 10:
      new_list.append(n)
  print(new_list)
less_than()

def squared_list():
  squared = []
  for n in list_of_ints:
    val = n**2
    squared.append(val)
  print(squared)
squared_list()

unduped = list(set(list_of_ints))
print(unduped)
print(len(unduped))

avg = sum(list_of_ints) / len(list_of_ints)
print(avg)

minimum = min(list_of_ints)
maximum = max(list_of_ints)


# Exercise 4
paragraph = 'Coding creates a set of instructions for computers to follow. These instructions determine what actions a computer can and cannot take. Coding allows programmers to build programs, such as websites and apps. Computer programmers can also tell computers how to process data in better, faster ways.'

total_char = len(paragraph)
print(total_char)

number_of_sentences = paragraph.count('.')
print(number_of_sentences)


def count_words():
  word_counter = 0
  for word in paragraph.split():
    word_counter +=1
  print(word_counter)
count_words()

def unique_words():
  og_str = []
  for word in paragraph.split():
    clean_word = word.strip(string.punctuation).lower()
    if clean_word in og_str:
      continue
    else:
      og_str.append(clean_word)
  print(len(og_str))
unique_words()

# Exercise 4
def word_frequency(input: str):
  counts = {} # word as key. Count as val
  cleaned_input = input.lower().replace("?", "").replace(",", "").replace(".", "").split()
  for word in cleaned_input:
    if word in counts:
      counts[word] += 1
    else:
      counts[word] = 1
  print(counts)
word_frequency('New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.')