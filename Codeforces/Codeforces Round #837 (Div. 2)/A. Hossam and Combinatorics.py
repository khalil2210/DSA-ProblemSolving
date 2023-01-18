import math
result=[]
t=int(input())
for i in range(t):
    n=int(input())
    ai=list(map(int,input().split(" ")))
    mi=min(ai)
    ma=max(ai)
    maxi=ai.count(ma)
    mini=ai.count(mi)
    if(mi==ma):
        result.append(math.ceil((n-1)*(n/2))*2)
    else:
        result.append(maxi*mini*2)
for i in result:
    print(i)
