import numpy as np

arr = np.random.randint(1, 1001, size=(3, 4))
print(arr)

arr2 = np.copy(arr)
arr2[arr2 > 500] = 0
print(arr2)

