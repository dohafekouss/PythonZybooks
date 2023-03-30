yearlyValues=[]

for i in range(0,12):
    i=int(input())
    yearlyValues.append(i)

for i in range(0,12,4):
    print(yearlyValues[i],end=" ")
    print(yearlyValues[i+1], end=" ")
    print(yearlyValues[i+2], end=" ")
    print(yearlyValues[i+3])