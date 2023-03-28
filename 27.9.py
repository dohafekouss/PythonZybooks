userMonth = int(input())
userDay = int(input())
userYear = int(input())

if ((userMonth == 12) and(userDay == 31)):
    nextMonth = 1
    nextDay   = 1
    nextYear  = userYear + 1

elif (((userMonth == 1) or (userMonth == 3) or (userMonth == 5) or (userMonth == 7) or (userMonth == 8) or (userMonth == 10)) and (userDay == 31) ):
    nextMonth = userMonth + 1
    nextDay   = 1
    nextYear  = userYear