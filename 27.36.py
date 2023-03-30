chptList = [False] * 16
includeChpt = False
atLeastOne = False

for i in range(1, 16):
    includeChpt = bool(input())
    if includeChpt:
        chptList[i] = True
    else:
        chptList[i] = False
i = 1
while i <= 15:
    if chptList[i]:
        print(i, end='')
        atLeastOne = True
        if (i <= 13) and chptList[i+1] and chptList[i+2]:
            j = i + 2
            while (j <= 14) and chptList[j+1]:
                j += 1
            print('-', j, end=' ')
            i = j + 1
        else:
            print(' ', end='')
        i += 1
    else:
        i += 1
if not atLeastOne:
    print('None', end=' ')
print()