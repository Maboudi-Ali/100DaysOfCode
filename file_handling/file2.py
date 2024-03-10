with open('data.txt', 'r') as f:
    for line in f.readlines():
        print(' '.join([x.strip() for x in line.split()]))

