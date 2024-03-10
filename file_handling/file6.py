s = 0
c = 0
with open('numbers.txt', 'r') as f:
    for x in f.readlines():
        s += int(x.replace('\n', ''))
        c += 1

print(f'sum: {s}')
print(f'mean: {s / c}')

