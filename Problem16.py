def problem16():
    num = pow(2, 1000)
    sum = 0

    while num >= 10:
        sum += num % 10
        num //= 10

    sum += num

    print(sum)

problem16()
