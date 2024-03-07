def digit_sum_recursive(num, sum=0):
    if num // 10 == 0:
        return num % 10 + sum
    else:
        sum += num % 10
        num //= 10
        return digit_sum_recursive(num, sum)


print(digit_sum_recursive(int(input())))

