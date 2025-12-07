
import pandas as pd
import numpy as np
"""

random_array = np.random.rand(5, 5)
print(random_array)
max_val = random_array.max()
print(max_val)
index_of_max = np.where(random_array == max_val)   
print(index_of_max)

random_array[index_of_max] = 0


print(random_array)


random_array_1 = np.random.randint(5)
random_array_2 = np.random.randint(5)

common_elements = np.intersect1d(random_array_1, random_array_2)
print(common_elements)



some_arr = np.random.rand(10)
print(some_arr)

asc_sort = np.sort(some_arr)
dec_sort = asc_sort[::-1]
print(asc_sort)
print(dec_sort)

"""

gen_random_arr = np.random.rand(4, 4)
print(gen_random_arr)


border_arr = np.zeros((5, 5))
print(border_arr)

border_arr[0, :] = 1
border_arr[:, 0] = 1
border_arr[-1, :] = 1
border_arr[:, -1] = 1

print(border_arr)