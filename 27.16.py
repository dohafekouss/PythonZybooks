userInt=int(input())
validSum=0
validNum=0
invalidNum=0
averageNum=0
while (userInt != 0):
    if ((userInt >= 2) and (userInt <= 12)):
        validSum += userInt;
        validNum += 1;
    elif (userInt != 0):
        invalidNum += 1;
    else:
        pass
    userInt=int(input())

if (validNum > 0):
    averageNum=validSum/validNum


print("Average: ",averageNum)
print("Valid: ",validNum)
print("Invalid: ",invalidNum)