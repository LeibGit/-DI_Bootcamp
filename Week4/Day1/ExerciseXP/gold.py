import pandas as pd
import numpy as np

matrix_ex = np.array([[1, 2, 3],
                        [4, 5, 6], 
                        [7, 8, 9]])
print(matrix_ex)


ran_matrix = np.random.rand(5, 5)
print(ran_matrix.min())
print(ran_matrix.max())

arr = np.array([[1, 2, 3], 
                [4, 5, 6], 
                [7, 8, 9]])
mean = arr.mean()
std_dev = arr.std()

normalized_matrix = (arr - mean) / std_dev
print(normalized_matrix)

print(np.linspace(0, 10, 50))

arr_1 = np.arange(15).reshape(5, 3)
arr_2 = np.arange(6).reshape(3, 2)

res = np.dot(arr_1, arr_2)
print(res)

arr_3 = np.array([[1, 2], [8, 9]])
arr_4 = np.array([[6, 7], [10, 7]])

res = arr_3 @ arr_4
print(res)