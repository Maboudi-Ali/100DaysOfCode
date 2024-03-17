# scalar function to array function
import numpy as np

def maxx(x, y):
    if x >= y:
        return x
    return y


def pair_max(x, y):
    maximum = [maxx(a, b) for a, b in map(lambda a, b: (a, b), x, y)]
    return np.array(maximum)

arr1 = np.random.randint(range(1, 6), 8)
arr2 = np.random.randint(range(1, 6), 8)
print(arr1, arr2, pair_max(arr1, arr2))

