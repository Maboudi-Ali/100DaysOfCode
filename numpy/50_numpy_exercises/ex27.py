import numpy as np

print(arr := np.random.randint(1, 11, (3, 4)))
print(np.mean(arr))
print(np.mean(arr, axis=0))
print(np.mean(arr, axis=1))

print(np.median(arr))
print(np.std(arr))


