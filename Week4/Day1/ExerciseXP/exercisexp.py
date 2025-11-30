import numpy as np

# exercise 1
my_arr = np.arange(10)
print(my_arr)

# exercise 2
some_list = [3.14, 2.17, 0, 1, 2]
new_arr = np.array(some_list, dtype=int)
print(new_arr)

# Exercise 3
arr = np.arange(1, 10).reshape(3, 3)
print(arr)

# Exercise 4
mutli_dem_arr = np.random.rand(4, 5)
print(mutli_dem_arr)

# Exercise 5
array = np.array([[21,22,23,22,22],
                  [20, 21, 22, 23, 24],
                  [21,22,23,22,22]])

print(array[1, :])

# Exercise 6
some_array = np.arange(0, 10)
print(some_array[::-1])

# Exercise 7
matrix = np.identity(4)
print(matrix)

# Exercise 8
some_ran_arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(some_ran_arr.sum())
print(np.mean(some_ran_arr))

# Exercise 9
struct_arr = np.arange(1, 21).reshape(4, 5)
print(struct_arr)  

# exercise 10
some_ran_arr_two = np.array([1, 3, 5, 7, 9])

returned_arr = []
for n in some_ran_arr_two:
    if n % 2 != 0:
        returned_arr.append(n)
    else:
        continue
print(returned_arr)