n = int(input("Enter an integer:"))
if (n<0):
    n=-n
print("Sequence:",end=" ")
for i in range(-n,n+1):
    print(i,end=" ")