import math


# Returns true if the number is prime
def isPrime(num):
    limit = math.floor(math.sqrt(num)) + 1

    for i in range(2, limit):
        if num % i == 0:
            return False

    return True


def problem7():

    # starts the count at 2, because 1 and 2 have already been counted
    count = 2

    # the first number to be checked is actually three, because 2 is added
    # before checking
    currentNumber = 1

    while count <= 10001:
        # the only prime number that is also even is 2, so this makes sure to
        # test only odd numbers
        currentNumber += 2
        if isPrime(currentNumber):
            count += 1

    print(currentNumber)

problem7()
