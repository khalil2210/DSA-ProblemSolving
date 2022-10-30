t=int(input())
result=[]
for i in range(t):
    n,k=list(map(int,input().split(" ")))
    ai=list(map(int,input().split(" ")))
    if((k==1)&(ai.count(1)==n)):
        result.append('YES')
    elif((ai.count(1)>=1)&(k>1)):
        result.append('YES')
    else:
        result.append('NO')
for i in result:
    print(i)
