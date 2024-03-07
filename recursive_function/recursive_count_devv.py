def recursive_count(lst, element, count=0):
    if lst:
        if lst[-1] == element:
            count += 1
        return recursive_count(lst[:-1], element, count)
    else:
        return count


print(recursive_count([1, 2, 3, 4, 7, 4, 4, 3, 2, 3, 2, 6, 8, 9], 4))

