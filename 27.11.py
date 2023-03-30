firstName1=input()
lastName1=input()
firstName2=input()
lastName2=input()
firstName3=input()
lastName3=input()

if (firstName1 == "none"):
    print("TBD")
elif (firstName2 == "none"):
    print((firstName1[0])+". "+lastName1)

elif (firstName3 == "none"):
    print(lastName1 +" / "+lastName2)

else:
    print(lastName1+" / " +lastName2+" / ...")
