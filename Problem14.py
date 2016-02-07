def getCollatzLength(num):
    pair = [num]
    length = 1
    while num != 1:
        if num % 2 == 0:
            num //= 2
        else:
            num = num * 3 + 1
        length += 1

    pair.append(length)

    return pair


def problem14():

    limit = 1000000

    maxPair = [1, 1]

    for i in range(1, limit):
        tempPair = getCollatzLength(i)
        if tempPair[1] > maxPair[1]:
            maxPair = tempPair

    print("The number is %s with a length of %s." % (maxPair[0], maxPair[1]))

problem14()
