numInts = int(input())

for i in range(numInts):
    if i > 0:
        print(", ", end="")
    currInt = int(input())
    print(currInt, end="")

print(".")