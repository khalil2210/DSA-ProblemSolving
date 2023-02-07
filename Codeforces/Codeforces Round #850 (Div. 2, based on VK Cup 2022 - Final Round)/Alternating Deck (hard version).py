t=int(input())
result=[]
for i in range(t):
    n=int(input())
    ai=list(map(int,input().split(" ")))
    ai.sort()
    ref=[1]
    if(n==1):
        result.append(ai[0]-1)
    else:
        for j in range(0,n-1):
            if(ai[j+1]>=ref[-1]+1):
                ref.append(ref[-1]+1)
            else:
                ref.append(ref[-1])
        res=0
        #print(ref)
        for j in range(n):
            if(ai[j]>ref[j]):
                res+=(ai[j]-ref[j])
        result.append(res)
for i in result:
    print(i)




