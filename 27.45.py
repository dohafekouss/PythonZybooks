def DigitToWord(digitIn):
    if digitIn == 0:
        wordOut = ""
    elif digitIn == 1:
        wordOut = "one"
    elif digitIn == 2:
        wordOut = "two"
    elif digitIn == 3:
        wordOut = "three"
    elif digitIn == 4:
        wordOut = "four"
    elif digitIn == 5:
        wordOut = "five"
    elif digitIn == 6:
        wordOut = "six"
    elif digitIn == 7:
        wordOut = "seven"
    elif digitIn == 8:
        wordOut = "eight"
    elif digitIn == 9:
        wordOut = "nine"
    else:
        wordOut = "error"
    return wordOut


def TensDigitToWord(digitIn):
    if digitIn == 0:
        wordOut = "error"
    elif digitIn == 1:
        wordOut = "error"
    elif digitIn == 2:
        wordOut = "twenty"
    elif digitIn == 3:
        wordOut = "thirty"
    elif digitIn == 4:
        wordOut = "forty"
    elif digitIn == 5:
        wordOut = "fifty"
    elif digitIn == 6:
        wordOut = "sixty"
    elif digitIn == 7:
        wordOut = "seventy"
    elif digitIn == 8:
        wordOut = "eighty"
    elif digitIn == 9:
        wordOut = "ninety"
    else:
        wordOut = "error"
    return wordOut

def TwoDigitNumToWords(numIn):
    onesDigit = numIn % 10
    tensDigit = numIn // 10

    return TensDigitToWord(tensDigit) + " " + DigitToWord(onesDigit)
userNum = int(input())
print(TwoDigitNumToWords(userNum))
