userText=input()
i=0
while ((i < len(userText)) and(userText[i] == ' ')):
    i=i+1;
if (i == len(userText)):
    pass

j = len(userText) - 1;
while ((j >= 0) and (userText[j] == ' ')):
    j=j-1

cleanedText=""
for n in range(i,j+1):
    cleanedText=cleanedText+userText[n]

print(cleanedText)
