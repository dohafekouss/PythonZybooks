throwValues = [0] * 21
frameScores = [0] * 10
t = 0
f = 0
for t in range(21):
    throwValues[t] = int(input())
t = 0
for f in range(9):
    frameScore = 0
    frameScore += throwValues[t]
    if frameScore == 10:
        frameScore += throwValues[t + 1] + throwValues[t + 2]
    else:
        t += 1
        frameScore += throwValues[t]
        if frameScore == 10:
            frameScore += throwValues[t + 1]
    t += 1
    if f > 0:
        frameScore += frameScores[f - 1]
    frameScores[f] = frameScore
frameScores[f] = frameScores[f - 1] + throwValues[t] + throwValues[t + 1] + throwValues[t + 2]

for f in range(10):
    print(frameScores[f], end=" ")
print()