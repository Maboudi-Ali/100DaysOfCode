# indices of matchin positions in two arrays 
import numpy as np

arr1 = np.random.choice([1, 2, 3], size=(5, 4)) 
arr2 = np.random.choice([1, 2, 3], size=(5, 4)) 
print(arr1, arr2, sep='\n')
print(indices := np.dstack(np.where(arr1 == arr2)))
print(np.where(arr1 == arr2))
print(indices.squeeze())

