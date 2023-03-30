def SimulateLine(customerArrivals):
    lineLength = 0
    for arrival in customerArrivals:
        if lineLength > 0:
            lineLength -= 1
        lineLength += arrival
        print(lineLength, end=' ')
    print()
customerArrivals = list(map(int, input().split()))

SimulateLine(customerArrivals)