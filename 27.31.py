listInts=[]
listNegInts=[]

for i in range(0,6):
    i=int(input())
    listInts.append(i)

for i in range(0,6):
    if(listInts[i]<0):
        listNegInts.append(listInts[i])

print(len(listNegInts))
for i in range (0,len(listNegInts)):
    print(listNegInts[i])