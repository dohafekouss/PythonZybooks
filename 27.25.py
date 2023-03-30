aisMinimum=float(input())
rowGPA=0


def decimal_range(start, stop, increment):
    while start < stop:
        yield start
        start =start+ increment
for i in decimal_range(3.0,4.1,0.1):
    rowTestScore = 1600.0 * (aisMinimum / 100.0) - 1600.0 * 2.5 * (rowGPA / 4.0);
    print(rowGPA," ",rowTestScore)
