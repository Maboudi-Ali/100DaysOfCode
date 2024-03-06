import time


def fib_gen():
    first = 0
    yield first
    second = 1
    yield second
    while True:
        third = first + second
        yield third
        time.sleep(1)
        first, second = second, third

for x in fib_gen():
    print(x)
