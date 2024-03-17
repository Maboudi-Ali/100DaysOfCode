# percentiles
import numpy as np

arr = np.random.randint(1, 100, (6, 8))
print(arr)
print(np.percentile(arr, q=[3, 64, 87]))

