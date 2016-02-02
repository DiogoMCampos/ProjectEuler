from math import sqrt


# a^2 + b^2 = c^2
# a + b + c = 1000
# (1000 - a - b)^2 = a^2 + b^2
# 1000 * (1000 - a - b) - 1000a - 1000b + 2 * a * b = 0
# 1000000 - 1000a - 1000a - 1000b - 1000b + 2 * a * b = 0
# 2 * (500000 - 1000a - 1000b + a * b) = 0
# 500000 - 1000a - 1000b + a * b = 0
# 500000 - 1000a - 1000b = - a * b
# 1000 * (500 - a - b) = - a * b
def problem9():
    found = False
    for a in range(1, 999):
        # since a != 0, b != 0, c 1=, 998 is the maximum for each
        # since (500 - a - b) must be negative, a + b > 500
        # therefore, for each a, b > 500 - a
        for b in range(500 - a, 999):
            if 1000 * (500 - a - b) == -a * b:
                found = True
                break
        if found:
            break

    c = int(sqrt(pow(a, 2) + pow(b, 2)))

    print(a * b * c)

problem9()
