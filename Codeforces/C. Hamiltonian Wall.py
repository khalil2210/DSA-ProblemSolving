def checkPath(row,c1,c2,n):
    for i in range(n-1):
        if((c1[i+1]=='B')&((c2[i+1]=='B'))&(row=='UP')):
            row="Down"
        elif((c1[i+1]=='B')&((c2[i+1]=='B'))&(row=='Down')):
            row="UP"
        elif((row=="UP")&(c1[i+1]=='W')):
            return "NO"
        elif((row=="Down")&(c2[i+1]=='W')):
            return "NO"
    return "YES"

t=int(input())
result=[]
for i in range(t):
    n=int(input())
    c1=input()
    c2=input()
    if((c1[0]=='B')&(c2[0]=='B')):
        if((checkPath("Down",c1,c2,n)=="YES")|(checkPath("UP",c1,c2,n)=="YES")):
            result.append("YES")
        else:
            result.append("NO")
    elif((c1[0]=='W')&(c2[0]=='B')):
        result.append(checkPath("Down",c1,c2,n))
    else:
        result.append(checkPath("UP",c1,c2,n))
for i in result:
    print(i)

