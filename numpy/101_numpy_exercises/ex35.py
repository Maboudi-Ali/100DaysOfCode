# drop missing value containing rows
import numpy as np

arr = np.random.randint(1, 10, (5, 5)).astype(float)
n_missing = np.random.randint(1, 5)

for i in range(n_missing):
    pos = (np.random.randint(5),
           np.random.randint(5))
    print(pos)
    arr[pos[0], pos[1]] = np.nan

print(arr)
nan_rows = np.sum(np.isnan(arr), axis=1).astype(bool)
print(nan_rows)
print(arr[~nan_rows])

