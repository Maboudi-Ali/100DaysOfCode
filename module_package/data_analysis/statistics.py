def mean(lst):
    return sum(lst) / len(lst)


def median(lst):
    lst.sort()
    t = len(lst)
    if t % 2:
        return lst[t // 2]
    else:
        return (lst[t // 2 - 1] + lst[t // 2]) / 2


def standard_deviation(lst):
    mu = mean(lst)
    n = len(lst)
    var = sum(map(lambda x: (x - mu) ** 2 / n, lst))
    return var ** 0.5

