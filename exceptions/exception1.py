def sum(lst):
    s = 0
    for i in lst:
        try:
            s += i

        except TypeError:
            continue

    return s

print(sum([1, 3, 5, 'ali']))

