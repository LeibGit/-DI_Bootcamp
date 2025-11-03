# Challenge #1
number = int(input("Enter a number: "))
length = int(input("Enter a length: "))

for i in range(length + 1):
  print(number*i)

# Challenge #2
string = str(input("Enter a string: "))
res = [string[0]]

for char in string:
  if char in res[-1]:
    continue
  else:
    res.append(char)
final_string = ''.join(res)
print(final_string)