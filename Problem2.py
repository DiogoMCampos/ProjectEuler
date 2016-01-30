def problem2():
    n = 0
    x0 = 1
    x1 = 2
    x2 = x0 + x1

    while x1 < 4000000:
        if (x1 % 2 == 0):
            n += x1
        x0 = x1
        x1 = x2
        x2 = x0 + x1

    print(n)

problem2()
