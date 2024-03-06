def cum_sum(lst):
    i = 0
    sum = 0
    while i < len(lst):
        sum += lst[i]
        yield sum
        i += 1


for x in cum_sum(range(1, 11)):
    print(x)
