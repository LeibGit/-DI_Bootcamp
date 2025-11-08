MATRIX_STR = '''
7ir
Tsi
h%x
i ?
sM# 
$a 
#t%''' 

# initialize a new list
grid = []

temp_str = ''
# split each line and save it as its own variable in a list
array = MATRIX_STR.splitlines()
array.remove('')
for row in array:
    grid.append(list(row))
print(grid)
for row in grid:
    if row[0].isalpha():
        temp_str += row[0]
    print(temp_str)
for row in grid:
    if row[1].isalpha():
        temp_str += row[1]
    print(temp_str)
for row in grid:
    if row[2].isalpha():
        temp_str += row[2]
    print(temp_str)