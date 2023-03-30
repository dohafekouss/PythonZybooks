passengerAge=input()
carryOns=input()
checkedBags=input()

if (int(passengerAge) >= 60):
    airFare = 290
elif (int(passengerAge) <= 2):
    airFare = 0
else:
    airFare = 300

if (int(carryOns) > 0):
    airFare += 10;

if (int(checkedBags) == 2):
    airFare += 25;
elif (int(checkedBags) >= 3):
    airFare += 25 + (int(checkedBags) - 2) * 50;

print(airFare)