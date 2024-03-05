lst = [1, 3, 4, 7]
even = lambda x: x % 2 == 0
odd = lambda x: x % 2 == 1
count_odd_even = lambda lst: (len(list(filter(even, lst))), len(list(filter(odd, lst))))
print(count_odd_even(lst))
