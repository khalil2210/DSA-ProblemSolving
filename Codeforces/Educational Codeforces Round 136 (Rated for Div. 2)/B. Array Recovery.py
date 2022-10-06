import math
t=int(input())
result=[]
for i in range(t):
    n=int(input())
    d=list(map(int,input().split(" ")))
    multiplecases=False
    a=[d[0]]
    ch=str(d[0])+" "
    j=1
    while((j<n)&(multiplecases==False)):
        if(d[j]==0):
            a.append(a[j-1])
            ch+=str(a[j-1])+" "
        elif(a[j-1]>=d[j]):
            multiplecases=True
        else:
            a.append(d[j]+a[j-1])
            ch+=str(a[j])+" "
        j+=1
    if(multiplecases==False):
        result.append(ch)
    else:
        result.append('-1')
for i in result:
    print(i)
