# reverse rows 
import numpy as np

arr = np.arange(25).reshape(5, 5)
print(arr)

arr[: , :] = arr[::-1 , :]
print(arr)

