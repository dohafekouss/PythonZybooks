import math
tvDiagonal = int(input())

for tvWidth in range(1, tvDiagonal):
    tvHeight = math.sqrt(tvDiagonal**2 - tvWidth**2)
    if tvWidth > tvHeight:
        print(tvWidth, tvHeight)