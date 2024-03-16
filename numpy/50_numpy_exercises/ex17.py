# swapping rows 
import numpy as np

arr = np.arange(12).reshape(3, 4)
print(arr)

arr[[0, 1], :] = arr[[1, 0], :]
print(arr)

