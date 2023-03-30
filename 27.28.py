listSize=int(input())
currNum=0
isSorted=True
for i in range(0,listSize):
    prevNum=currNum
    currNum=int(input())
    if i>0:
        if(currNum<prevNum):
            isSorted=False

if (isSorted==True):
    print("Sorted")
else:
    print("Unsorted")