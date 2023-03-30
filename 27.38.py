listNums = []
while True:
    try:
        currNum = int(input())
        listNums.append(currNum)
    except:
        break

listSize = len(listNums)
for i in range(listSize // 2):
    tmp = listNums[i]
    listNums[i] = listNums[listSize - i - 1]
    listNums[listSize - i - 1] = tmp

for i in range(listSize):
    print(listNums[i], end=" ")
print()