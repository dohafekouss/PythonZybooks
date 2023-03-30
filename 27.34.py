userValues = [0] * 10
i = 0
minVal = 0
maxVal = 0
sumVals = 0
curVal = 0
for i in range(10):
    userValues[i] = int(input())
minVal = userValues[0]
maxVal = userValues[0]
sumVals = 0
for i in range(10):
    curVal = userValues[i]
    if curVal < minVal:
        minVal = curVal
    if curVal > maxVal:
        maxVal = curVal
    sumVals += curVal

print(minVal, maxVal, sumVals / 10.0)