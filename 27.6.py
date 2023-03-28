userCaption = input()
lastIndex=len(userCaption)-1
lastChar=userCaption[lastIndex]

if ((lastChar == '!') or (lastChar == '?')):
    pass
elif (lastChar == ','):
    userCaption[lastIndex] = '.'

elif (lastChar != '.'):
    userCaption=userCaption+'.'
elif ((lastIndex > 0) and (lastChar == '.') and (userCaption[lastIndex - 1] == '.')):
    if ((lastIndex > 1) and (userCaption[lastIndex - 2] == '.')):
        pass
    else:
        userCaption=userCaption[:-1]

print(userCaption)