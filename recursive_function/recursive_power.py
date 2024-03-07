def recursive_power(num, power):
    if power:
        power -= 1
        return num * recursive_power(num, power)
    else:
        return 1


print(recursive_power(4, 5))
