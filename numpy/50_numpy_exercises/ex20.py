# 2d array of random numbers between 5 and 10
import numpy as np

arr = 5 * np.random.rand(3, 4) + 5
print(arr)

second_arr = np.random.uniform(5, 10, (4, 3))
print(second_arr)

