import math


# Returns list of factors of num
def getFactors(num):
    factorsList = [1, num]
    limit = math.floor(math.sqrt(num)) + 1

    for i in range(2, limit):
        if num % i == 0:
            factorsList.append(i)
            factorsList.append(num // i)

    return factorsList


def problem12():
    found = False
    currentNumber = 0
    i = 1

    while not found:
        currentNumber += i
        factorsList = getFactors(currentNumber)

        if len(factorsList) > 500:
            print(currentNumber)
            found = True

        i += 1

problem12()
