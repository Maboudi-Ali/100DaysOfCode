# correlation between two columns of an array
import numpy as np

arr = np.random.randint(1, 10, size=(5, 5))
print(arr)
print(np.corrcoef(col1 := arr[:, 2], col2 := arr[:, 4]))
print(col1, col2)
print(np.cov([col1, col2, arr[:, 0]]))

