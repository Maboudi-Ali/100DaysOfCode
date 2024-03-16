# swap two columns 
import numpy as np

arr = np.random.randint(1, 10, size=(3, 4))
print(arr)

arr[:, [0, 1]] = arr[:, [1, 0]]
print(arr)

