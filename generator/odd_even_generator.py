import sys


def num_generator(option):
    num = 1
    if option == 'even':
        num = 2
    while True:
        yield num
        num += 2


option = sys.argv[1]
if option not in ['odd', 'even']
    print('please give and argument: odd/even')
else:
    for x in num_generator(option): print(x)
