plate_number = input()
c1, c2, c3 = plate_number[0], plate_number[1], plate_number[2]
i1, i2, i3 = plate_number[3], plate_number[4], plate_number[5]
carry_needed = False

if i3 < '9':
    i3 = chr(ord(i3) + 1)
else:
    i3 = '0'
    carry_needed = True


if carry_needed:
    if i2 < '9':
        i2 = chr(ord(i2) + 1)
        carry_needed = False
    else:
        i2 = '0'
        carry_needed = True


if carry_needed:
    if i1 < '9':
        i1 = chr(ord(i1) + 1)
        carry_needed = False
    else:
        i1 = '0'
        carry_needed = True

if carry_needed:
    if c3 < 'Z':
        c3 = chr(ord(c3) + 1)
        carry_needed = False
    else:
        c3 = 'A'
        carry_needed = True

if carry_needed:
    if c2 < 'Z':
        c2 = chr(ord(c2) + 1)
        carry_needed = False
    else:
        c2 = 'A'
        carry_needed = True
if carry_needed:
    if c1 < 'Z':
        c1 = chr(ord(c1) + 1)
        carry_needed = False
    else:
        c1 = 'A'
        carry_needed = True

print(c1 + c2 + c3 + i1 + i2 + i3)