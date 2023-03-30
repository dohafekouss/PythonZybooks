idToFind = input()
dbId = ""
dbFirstName = ""
dbLastName = ""
try:
    with open("CustomerDb.txt") as customerDb:
        while True:
            line = customerDb.readline().strip()
            if not line:
                break
            dbId, dbFirstName, dbLastName = line.split()
            if dbId == idToFind:
                print(dbFirstName, dbLastName)
                break
        else:
            print("Not found")
except FileNotFoundError:
    print("Could not open CustomerDb.txt")