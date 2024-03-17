import numpy as np

arr = np.arange(10001)
print(arr[-1000:])

arr[arr > 9000] = 0
print('-' * 20)
print(arr[-1000:])

