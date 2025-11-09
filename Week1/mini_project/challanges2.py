def pattern_one(rows: int):
    for i in range(1, rows + 1):
        stars = 2 * i - 1
        print('*' * stars)
pattern_one(rows=3)

def pattern_two(rows: int):
    for i in range(1, rows + 1):
        stars = i 
        print('*' * stars)
pattern_two(rows=5)

def pattern_three(rows: int):
    pattern_two(rows=5)
    for i in range(rows - 1, 0, -1):
        print('*' * i)
pattern_three(rows=5)

# initializing a list of ints
my_list = [2, 24, 12, 354, 233]
# for each number up until 4
for i in range(len(my_list) - 1):
    # assigning the current number as the min
    minimum = i
    for j in range( i + 1, len(my_list)):
        if(my_list[j] < my_list[minimum]):
            minimum = j
            if(minimum != i):
                my_list[i], my_list[minimum] = my_list[minimum], my_list[i]
print(my_list)