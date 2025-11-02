x = 5
y = 10
z = 0
word1 = "Hello"
word2 = "World"

def check_x_y_z():
  if x < y and y > z:
    return True
  else:
    return False
print(check_x_y_z())

def check_words():
  if word1 != word2:
    return True
  else:
    return False
  
def check_bool():
  print(bool(z))
  print(bool(word1))