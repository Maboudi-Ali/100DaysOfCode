# extract a column from a 1d array of tuples
import numpy as np
import random

number = random.randint
lst = [(number(1, 10), number(1, 10), number(1, 10)) for i in range(5)]
arr = np.array(lst)
print(arr)
print(list(map(lambda x: x[2], arr)))

