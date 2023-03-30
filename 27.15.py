initialVelocity=int(input())
rocketHeight=0
timeSinceLaunch=0
while rocketHeight>=0:
    print(timeSinceLaunch," ",rocketHeight)
    timeSinceLaunch=timeSinceLaunch+1

    rocketHeight = (initialVelocity * timeSinceLaunch) - (5 * timeSinceLaunch * timeSinceLaunch)