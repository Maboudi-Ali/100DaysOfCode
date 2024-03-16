# reverse columns
import numpy as np

arr = np.random.randint(1, 10, (3, 4))
print(arr)

arr[:, :] = arr[:, ::-1]
print(arr)

