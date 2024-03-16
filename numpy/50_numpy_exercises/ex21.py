# print 3 decimal places
import numpy as np

normal_arr = np.random.normal(size=(3, 3))
print(normal_arr)

np.set_printoptions(precision=3)
print(normal_arr)

