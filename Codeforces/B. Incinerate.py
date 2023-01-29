t=int(input())
result=[]
for i in range(t):
    n,k=list(map(int,input().split(" ")))
    hi=list(map(int,input().split(" ")))
    pi=list(map(int,input().split(" ")))
    d={}
    for j in range(n):
        if(pi[j] not in d):
            d[pi[j]]=hi[j]
        elif(hi[j]>d[pi[j]]):
            d[pi[j]]=hi[j]
    #list of powers
    l=list(d.keys())
    l.sort()
    totalDamage=0
    for j in l:
        d[j]-=totalDamage
        while((d[j]-k>0)):
            d[j]-=k
            totalDamage+=k
            k-=j
            if(k<=0):
                break
    if(k>0):
        result.append("YES")
    else:
        result.append("NO")
for i in result:
    print(i)
