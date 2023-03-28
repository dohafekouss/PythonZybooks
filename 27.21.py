userRows=int(input())
userCols=int(input())

print("<table>")
for i in range(0,userRows):
    print("<tr>",end=" ")
    for j in range(0,userCols):
        print("<td> c </td> ",end=" ")
    print("</tr>")
print("</table>")