from math import sqrt


def problem10():
    # based on the Sieve of Eratosthenes
    numberList = [True] * 2000000
    primesSum = 0

    numberList[0] = numberList[1] = False

    for (i, prime) in enumerate(numberList):
        if prime:
            primesSum += i

            if i <= sqrt(2000000):
                j = i * i
                while j < 2000000:
                    numberList[j] = False
                    j += i

    print(primesSum)


problem10()
