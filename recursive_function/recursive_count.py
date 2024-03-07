count = 0
def recursive_count(lst, element):
    global count
    if lst:
        if lst.pop() == element:
            count += 1
        return recursive_count(lst, element)
    else:
        return count


print(recursive_count([1, 2, 3, 4, 7, 4, 4, 3, 2, 3, 2, 6, 8, 9], 4))

