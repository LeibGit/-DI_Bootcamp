MATRIX_STR = '''
7ir
Tsi
h%x
i ?
sM# 
$a 
#t%''' 

grid = [list(MATRIX_STR[i:i+3]) for i in range(0, len(MATRIX_STR), 3)] 

for row in grid:
    for i in row:       
        print(row[0], row[1])