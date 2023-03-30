def GetAge(birthMonth, birthDay, birthYear, currMonth, currDay, currYear):
    currAge = currYear - birthYear
    if currMonth < birthMonth:
        currAge = currAge - 1
    elif currMonth == birthMonth:
        if currDay < birthDay:
            currAge = currAge - 1
    return currAge
birthMonth, birthDay, birthYear = map(int, input().split())
currMonth, currDay, currYear = map(int, input().split())
print(GetAge(birthMonth, birthDay, birthYear, currMonth, currDay, currYear))