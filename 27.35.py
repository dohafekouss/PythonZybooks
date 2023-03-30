userValues = [0] * 10
i = 0
curVal = 0
valCounts = [0] * 100
maxCount = 0
maxCountIndex = 0

for i in range(10):
    userValues[i] = int(input())

for i in range(10):
    curVal = userValues[i]
    if (curVal < 0) or (curVal > 99):
        print("Invalid input: ", curVal, " is not in 0-99")
        exit()

    valCounts[curVal] += 1
maxCount = valCounts[0]
maxCountIndex = 0
for i in range(100):
    if valCounts[i] > maxCount:
        maxCount = valCounts[i]
        maxCountIndex = i

print(maxCountIndex, maxCount)