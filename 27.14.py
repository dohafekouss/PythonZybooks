n = int(input("Enter an integer: "))

print("Sequence:",end=" ")

if (n<0):
    n=0

if ((n % 2) == 1):
    n = n - 1;

for i in range(n,-1,-2):
    print(i,end=" ")
