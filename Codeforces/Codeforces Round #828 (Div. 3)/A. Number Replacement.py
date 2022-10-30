t=int(input())
result=[]
for i in range(t):
    n=int(input())
    ai=list(map(int,input().split(" ")))
    s=input()
    test=['-1' for j in range(51)]
    res='YES'
    for j in range(n):
        if(test[ai[j]]=='-1'):
            test[ai[j]]=s[j]
        elif(test[ai[j]]!=s[j]):
            res='NO'
    result.append(res)
for i in result:
    print(i)


