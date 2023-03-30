def ActivityCalories(activityDone, minutesSpent):

    if (activityDone=="sit"):
        caloriesPerMinute=1.4
    elif (activityDone=="walk"):
        caloriesPerMinute=5.4
    elif (activityDone=="run"):
        caloriesPerMinute=13.0
    elif (activityDone=="bike"):
        caloriesPerMinute=6.8
    elif (activityDone=="swim"):
        caloriesPerMinute=8.7
    else:
        caloriesPerMinute=0.0
    print(caloriesPerMinute*minutesSpent)

userActivity=input()
userMinutes=int(input())


ActivityCalories(userActivity,userMinutes)
