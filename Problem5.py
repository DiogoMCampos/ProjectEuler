import math

# Returns true if the number is prime
def isPrime(num):
    limit = math.floor(math.sqrt(num)) + 1

    for i in range(2, limit):
        if num % i == 0:
            return False

    return True

# Returns the number of times the number 'num' appears in 'comparable'
def howMany(num, comparable):
    if isinstance(comparable, int):
        if comparable == num:
            return 1
        return 0
    else:
        times = 0
        for j in comparable:
            if j == num:
                times += 1
        return times

    return 0


def problem5():
    factors = []

    # prime numbers from 2 to 20
    primeNumbers = [2, 3, 5, 7, 11, 13, 17, 19]

    # prime factorization of every number from 2 to 20
    for i in range(2, 21):
        if isPrime(i):
            factors.append(i)
        else:
            tempList = []
            for j in primeNumbers:
                if i == 1:
                    break
                while i % j == 0:
                    i /= j
                    tempList.append(j)
            factors.append(tempList)

    primeMult = []

    # counts the highest power of each prime number
    for k in range(1, 21):
        count = 0
        for m in factors:
            times = howMany(k, m)
            if times > count:
                count = times
        primeMult.append(count)

    result = 1
    currentNumber = 1

    for prime in primeMult:
        if prime != 0:
            result *= pow(currentNumber, prime)

        currentNumber += 1

    print(result)


problem5()
