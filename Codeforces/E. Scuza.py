def maxInd(t,n,i):
    inf=0
    sup=n-1
    while(inf<=sup):
        if(t[sup]<=i):
            return sup
        mid=(inf+sup)//2
        if(t[mid]<=i):
            inf=mid
            sup-=1
        elif(t[mid>i]):
            sup=mid-1
    return -1





t=int(input())
result=[]
for i in range(t):
    n,q=list(map(int,input().split(" ")))
    steps=list(map(int,input().split(" ")))
    legs=list(map(int,input().split(" ")))
    maximum=[steps[0]]
    sums=[steps[0]]

    for s in range(1,n):
        sums.append(sums[s-1]+steps[s])
        if(steps[s]>maximum[s-1]):
            maximum.append(steps[s])
        else:
            maximum.append(maximum[s-1])
    ch=""
    for i in legs:
        a=maxInd(maximum,n,i)
        if(a==-1):
            ch+="0 "
        else:
            ch+=str(sums[a])+" "
    result.append(ch)
for i in result:
    print(i)
