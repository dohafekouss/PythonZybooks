hourAmPm=int(input())
minAmPm = int(input())

amPm=input()

if ((hourAmPm == 12) and (amPm == "am")):
    hour24 = 0;
elif ((amPm == "pm") and (hourAmPm != 12)):
    hour24 = hourAmPm + 12
else:
    hour24 = hourAmPm
if (hour24 < 10):
    print("0")

print(hour24,":")

if (minAmPm < 10):
    print("0")


print(minAmPm)
