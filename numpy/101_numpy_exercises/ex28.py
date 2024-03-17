# normalize an array with zero mean and unit variance 
import numpy as np

arr = np.random.randint(1, 11, (3, 8))
print(arr)
norm_arr = (arr - np.mean(arr)) / np.std(arr)
print(norm_arr)
np.set_printoptions(precision=3, suppress=True)

print(f'mean: {np.mean(norm_arr)}')
print(f'std: {np.std(norm_arr)}')

