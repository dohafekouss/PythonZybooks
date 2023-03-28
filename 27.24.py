userText=input()
inWord=False
wordCount=0
for i in range(0,len(userText)):
    if (userText[i] == ' '):
        inWord = False
    elif (inWord==False):
        wordCount += 1
        inWord = True
    else:
        pass

print(wordCount)