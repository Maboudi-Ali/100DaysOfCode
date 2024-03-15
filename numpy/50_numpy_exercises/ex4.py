import numpy as np

arr = np.random.choice(1000, 500000)
print(arr[np.logical_and(arr > 400, arr < 650)])

