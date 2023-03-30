listSize=int(input())

currNum=0
maxDiff = 0;
for i in range(0,listSize):
    prevNum = currNum;
    currNum=int(input())
    if (i > 0):
        currDiff = currNum - prevNum;
        if (currDiff < 0):
            currDiff = -currDiff;

        if (currDiff > maxDiff):
            maxDiff = currDiff;
print(maxDiff)
