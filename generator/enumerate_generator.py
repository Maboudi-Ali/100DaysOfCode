def enumerate(lst):
    i = 0
    while i < len(lst):
        yield i, lst[i]
        i += 1


print(enumerate(list(range(10, 100))))
for x in enumerate((list(range(10, 100)))):
    print(x)
