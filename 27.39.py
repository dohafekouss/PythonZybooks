def MaxFive(a, b, c, d, e):
    maxFound = a
    if b > maxFound:
        maxFound = b
    if c > maxFound:
        maxFound = c
    if d > maxFound:
        maxFound = d
    if e > maxFound:
        maxFound = e
    return maxFound

v, w, x, y, z = map(int, input().split())
maxVal = MaxFive(v, w, x, y, z)
print(maxVal)