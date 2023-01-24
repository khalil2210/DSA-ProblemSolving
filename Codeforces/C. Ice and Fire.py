t=int(input())
result=[]
for i in range(t):
    n=int(input())
    s=input()
    r=['1']
    for j in range(2,n):
        if(s[j-2]==s[j-1]):
            r.append(r[-1])
        else:
            r.append(str(j))
    result.append(" ".join(r))
for i in result:
    print(i)




