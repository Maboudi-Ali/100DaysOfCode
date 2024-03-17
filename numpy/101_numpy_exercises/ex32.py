# add elements at random places in array

import numpy as np

arr = np.random.randint(1, 10, 10)
print(arr)
k = int(input('how many random elements? '))
for i in range(k):
    idx = np.random.randint(0, len(arr))
    value = np.random.randint(1, 10)
    arr = np.insert(arr, idx, value)
    print(arr)

