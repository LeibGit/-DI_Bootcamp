import calendar


# Exercise 1 : Hello World-I love Python
print(("Hello World \n" * 4 + "I Love Python \n" * 4))

# Exercise 2: What Is The Season?
import calendar
prompt = int(input("Input a month 1-12: "))
month = calendar.month_name[prompt]
if prompt >= 3 and prompt <= 5:
  print('Spring runs from March (3) to May (5)')
elif prompt >=6 and prompt<=8:
  print("Summer runs from June (6) to August (8)")
elif prompt >= 9 and prompt <= 11:
  print("Autumn runs from September (9) to November (11)")
else:
  print("Winter runs from December (12) to February (2)")

# Exercise 4
my_text = """Lorem ipsum dolor sit amet, consectetur adipiscing elit, 
           sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
           Ut enim ad minim veniam, quis nostrud exercitation ullamco 
           laboris nisi ut aliquip ex ea commodo consequat. 
           Duis aute irure dolor in reprehenderit in voluptate velit 
           esse cillum dolore eu fugiat nulla pariatur. 
           Excepteur sint occaecat cupidatat non proident, 
           sunt in culpa qui officia deserunt mollit anim id est laborum."""
print(len(my_text))

# Exercise 5

def longest_input():
  count = 0
  array_of_sentences = ['o']
  letter = 'a'

  while count <= 5:
    prompt = str(input("Input the longest sentence you can without the letter A: ").lower())


    if letter in prompt:
      print("Failed. Enter a sentance without the letter a.")
      count += 1
    else:
      last_value = array_of_sentences[-1]
      if len(prompt) < len(last_value):
        print("Try again. this string is not longer than the last.")
      elif len(prompt) == len(last_value):
        print("Almost. Equal to your longest sentence.")
      else:
        print("Congrats, you have a new longest sentence.")
        array_of_sentences.append(prompt)
    count += 1
longest_input()