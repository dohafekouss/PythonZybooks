numItems=int(input())
listItem=[]
for i in range(numItems):
    currItem=int(input())
    listItem.append(currItem)

maxItem=listItem[0]
for i in range (numItems):
    if (listItem[i]>maxItem):
        maxItem=listItem[i]

print(maxItem)