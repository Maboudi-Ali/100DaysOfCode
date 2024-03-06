import time


def gen():
    i = 1
    while True:
        yield str(i) * i
        i += 1
        time.sleep(1)


for x in gen(): print(x)
