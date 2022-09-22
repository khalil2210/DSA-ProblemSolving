import math
t=int(input())
result=[]
for i in range(t):
    l,r=list(map(int,input().split(" ")))
    prime2=[]
    if((r%2==1)&(r-1>=l)):
        r-=1
    right=r
    j=2
    while(j<=int(math.sqrt(r))):
        if(r%j==0):
            prime2.append(j)
            r=r//j
            break
        else:
            j+=1

    prime2.append(r)
    if((l*prime2[0])>right):
        result.append("-1 -1")
    else:
        result.append(str(l)+" "+str(l*prime2[0]))
for i in result:
    print(i)

