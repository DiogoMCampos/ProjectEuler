def getNumberUn(x):
    if x == 9:
        return "nine"
    elif x == 8:
        return "eight"
    elif x == 7:
        return "seven"
    elif x == 6:
        return "six"
    elif x == 5:
        return "five"
    elif x == 4:
        return "four"
    elif x == 3:
        return "three"
    elif x == 2:
        return "two"
    elif x == 1:
        return "one"
    else:
        return ""


def getNumberDec(x):
    if x < 10:
        return getNumberUn(x)
    if x < 20:
        if x == 19:
            return "nineteen"
        elif x == 18:
            return "eighteen"
        elif x == 17:
            return "seventeen"
        elif x == 16:
            return "sixteen"
        elif x == 15:
            return "fifteen"
        elif x == 14:
            return "fourteen"
        elif x == 13:
            return "thirteen"
        elif x == 12:
            return "twelve"
        elif x == 11:
            return "eleven"
        elif x == 10:
            return "ten"
    else:
        if x <= 30:
            return "twenty" + getNumberUn(x - 20)
        elif x <= 40:
            return "thirty" + getNumberUn(x - 30)
        elif x <= 50:
            return "forty" + getNumberUn(x - 40)
        elif x <= 60:
            return "fifty" + getNumberUn(x - 50)
        elif x <= 70:
            return "sixty" + getNumberUn(x - 60)
        elif x <= 80:
            return "seventy" + getNumberUn(x - 70)
        elif x <= 90:
            return "eighty" + getNumberUn(x - 80)
        elif x < 100:
            return "ninety" + getNumberUn(x - 90)


def getNumberHun(x):
    if x < 100:
        return getNumberDec(x)

    writtenNumber = ""

    firstDigit = x // 100
    lastTwoDigits = x % 100

    writtenNumber = getNumberUn(firstDigit) + "hundredand"
    writtenNumber += getNumberDec(lastTwoDigits)

    return writtenNumber


def problem17():
    sum = 0

    for i in range(1, 999):
        sum += len(getNumberHun(i))
        
    sum += len("thousand")

    print(sum)

problem17()
