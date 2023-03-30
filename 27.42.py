def absVal(a):
    if a<0:
        return -a
    else:
        return a


def PickupMinutes(userX, userY, d1X, d1Y, d2X, d2Y, d3X, d3Y):

    dist1 = absVal(userX - d1X) + absVal(userY - d1Y)
    dist2 = absVal(userX - d2X) + absVal(userY - d2Y)
    dist3 = absVal(userX - d3X) + absVal(userY - d3Y)

    minDist = dist1
    if dist2 < minDist:
        minDist = dist2

    if (dist3 < minDist):
        minDist = dist3

    print(2 * minDist)

userX=int(input())
userY=int(input())
d1X=int(input())
d1Y=int(input())
d2X=int(input())
d2Y=int(input())
d3X=int(input())
d3Y=int(input())

PickupMinutes(userX,userY,d1X,d1Y,d2X,d2Y,d3X,d3Y)


