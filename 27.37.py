numItems = int(input())
listItems = []
for i in range(numItems):
    currItem = input()
    listItems.append(currItem)
longestSeqLength = 0
currSeqLength = 0
for i in range(numItems):
    if listItems[i] == "|":
        currSeqLength = 0
    else:
        currSeqLength += 1
        if currSeqLength > longestSeqLength:
            longestSeqLength = currSeqLength
print(longestSeqLength)