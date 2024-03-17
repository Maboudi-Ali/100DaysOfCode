# sorting
import numpy as np

arr = np.random.randint(1, 101, 100)
print(arr)
print(np.sort(arr))
print(np.sort(np.unique(arr))[-2])

