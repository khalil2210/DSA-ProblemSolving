t=int(input())
result=[]
for i in range(t):
    n,m=list(map(int,input().split(" ")))
    l=[n+1 for j in range(n+1)]
    l[0]="start :"
    for j in range(m):
        xiyi=list(map(int,input().split(" ")))
        xiyi.sort()
        if(xiyi[1]<l[xiyi[0]]):
            l[xiyi[0]]=xiyi[1]
    npairs=0
    for j in range(n-1,1,-1):
        if(l[j-1]>l[j]):
            l[j-1]=l[j]
        if(l[j]-j-1>0):
            npairs+=(l[j]-j-1)
    #first value
    if(l[1]-2>0):
        npairs+=(l[1]-2)
    result.append(npairs+n)
for k in result:
    print(k)

