from math import floor


def isPalindrome(num):
    strnum = str(num)
    length = len(strnum)
    maxVal = floor(length)

    for i in range(0, maxVal):
        if strnum[i] != strnum[length - 1 - i]:
            return False

    return True


def problem4():
    largestPalindrome = 0

    for i in range(1000, 100, -1):
        if largestPalindrome > i * 999:
            break
        for j in range(1000, 100, -1):
            if isPalindrome(i * j) and i * j > largestPalindrome:
                largestPalindrome = i * j

    print(largestPalindrome)

problem4()
