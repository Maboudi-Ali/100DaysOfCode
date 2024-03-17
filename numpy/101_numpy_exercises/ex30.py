# compute softmax_score of an array
import numpy as np

def softmax(arr):
    exp_arr = np.exp(arr)
    return exp_arr / np.sum(exp_arr)

arr = np.arange(4)
print(arr)
soft_arr = softmax(arr)
print(f'softmax arr: {soft_arr}')
print(f'sum of elements, softmax arr: {np.sum(soft_arr)}')

def sum_normalizer(arr):
    return arr / np.sum(arr)

sum_norm_arr = sum_normalizer(arr)
print(f'sum normalized arr: {sum_norm_arr}')
print(f'sum of elements, sum normalized arr: {np.sum(sum_norm_arr)}')

