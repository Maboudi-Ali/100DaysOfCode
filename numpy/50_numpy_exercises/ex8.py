import numpy as np
from ex7 import reshaped_arr as arr2


arr = np.zeros((5, arr2.shape[1]))
stacked = np.vstack([arr, arr2])
print(stacked)

