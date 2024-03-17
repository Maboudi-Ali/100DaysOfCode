# common items between two arrays

import numpy as np

arr1 = np.arange(5, 16)
arr2 = np.arange(10, 21)

print(np.intersect1d(arr1, arr2))

