import random

list_of_numbers = [random.randint(0, 10000) for _ in range(20000)]

target_number = 3728

sorted_list = sorted(list_of_numbers)

for x in list_of_numbers:
    for y in list_of_numbers:
        if x + y == target_number:
            print(f"{x} + {y} = {target_number}")