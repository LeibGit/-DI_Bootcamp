import random

prompt = str(input("Enter a 10 character string: ")).replace(" ", "")

if len(prompt) < 10:
  print("String not long enough.")
elif len(prompt) > 10:
  print("String too long.")
else:
  print("perfect string")
  print(f"First: {prompt[0]}, last: {prompt[-1]}")


arr = []
for char in prompt:
  arr.append(char)
  for i in arr:
    print(i, end="")
  print()


shuffle = list(prompt)
print(shuffle)

random.shuffle(shuffle)

shuffled = ''.join(shuffle)
print(shuffled)