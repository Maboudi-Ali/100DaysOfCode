# custom sequence without hardcoding
import numpy as np

arr = np.arange(1, 4)
custom = np.hstack([np.repeat(arr, 3), np.tile(arr, 3)])
print(custom)

