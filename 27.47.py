def CentsToDollarsCents(userCents):
    numDollars = userCents // 100
    numCents = userCents % 100
    return numDollars, numCents
userCents = int(input())
numDollars, numCents = CentsToDollarsCents(userCents)
print(numDollars, "dollars", numCents, "cents")