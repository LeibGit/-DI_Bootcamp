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
  