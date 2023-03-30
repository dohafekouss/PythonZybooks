binaryNum=[]

for i in range(8,0,-1):
    i = int(input())
    binaryNum.append(i)

digitWeight=1
decimalSum=0
for i in range(0,8):
    decimalSum=decimalSum+binaryNum[i]*digitWeight
    digitWeight*=2

print(decimalSum)