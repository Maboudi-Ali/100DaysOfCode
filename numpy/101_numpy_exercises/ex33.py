# getting positions of missing values in array

import numpy as np

arr = np.random.choice(np.append(np.random.randint(1, 100, 100).squeeze(), np.nan), size=25)
print(arr)
print(np.isnan(arr))

