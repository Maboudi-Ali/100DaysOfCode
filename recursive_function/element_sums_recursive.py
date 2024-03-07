def recursive_sum(lst):
    if lst:
        last_element = lst.pop()
        print(last_element)
        return last_element + recursive_sum(lst)
    else:
        return 0


print(recursive_sum([1, 4, 7, 9, 2]))
