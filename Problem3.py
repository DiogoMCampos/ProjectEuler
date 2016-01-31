from math import sqrt
from math import floor


def largestPrimeFactor(n):
    limit = floor(sqrt(n))

    for x in range(2, limit):
        if n % x == 0:
            return largestPrimeFactor(n / x)

    return n


def problem3():
    factor = largestPrimeFactor(600851475143)
    print(factor)

problem3()
