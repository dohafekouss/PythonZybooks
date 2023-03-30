totalInches = int(input())
feet = totalInches // 12
inches = totalInches - feet*12
print(str(feet) + "'" + str(inches) + "\"" )