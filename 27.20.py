from curses.ascii import isalpha, isdigit

userText = input()
lengthOK = False
hasLetter = False
hasNumber = False
hasSpecial = False

if (len(userText) >= 8):
    lengthOK = True


for i in range(0,len(userText)):
    c = userText[i];

    if (isalpha(c)):
        hasLetter = True;

    elif (isdigit(c)):
        hasNumber = True;

    elif ((c == '!') or (c == '#') or (c == '%')):
        hasSpecial = True

if (lengthOK==True and hasLetter==True and hasNumber==True and hasSpecial==True):
    print("OK")

else:
    if (lengthOK==False):
        print("Too short")
    if (hasLetter==False):
        print("Missing letter")
    if (hasNumber==False):
        print("Missing number")

    if (hasSpecial==False):
        print("Missing special")