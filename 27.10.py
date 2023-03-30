runwayNum = int(input())

runwayDeg = runwayNum * 10
if ((runwayDeg > 0 - 22.5) and (runwayDeg < 0 + 22.5)):
    runwayDirection = "north"

elif ((runwayDeg > 45 - 22.5) and (runwayDeg < 45 + 22.5)):
    runwayDirection = "northeast"
elif ((runwayDeg > 90 - 22.5) and(runwayDeg < 90 + 22.5)):
    runwayDirection = "east"
elif ((runwayDeg > 135 - 22.5) and (runwayDeg < 135 + 22.5)):
    runwayDirection = "southeast"
elif ((runwayDeg > 180 - 22.5) and (runwayDeg < 180 + 22.5)):
    runwayDirection = "south"

elif ((runwayDeg > 225 - 22.5) and (runwayDeg < 225 + 22.5)):
    runwayDirection = "southwest"

elif ((runwayDeg > 270 - 22.5) and (runwayDeg < 270 + 22.5)):
    runwayDirection = "west"

elif ((runwayDeg > 315 - 22.5) and (runwayDeg < 315 + 22.5)):
    runwayDirection = "northwest"


print(runwayDeg," degrees (",runwayDirection,")")