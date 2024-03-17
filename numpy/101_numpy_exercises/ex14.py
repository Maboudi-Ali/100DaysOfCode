# extracting all number between an specific range in an array

import numpy as np

arr = np.random.randint(1, 10000000, 60000)
print(arr)
print(filtered := arr[np.logical_and(arr > 100000,  arr < 210000)])
print((arr < 20).any())

