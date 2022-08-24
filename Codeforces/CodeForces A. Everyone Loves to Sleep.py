t=int(input())
result=[]
for i in range(t):
    n,H,M=list(map(int,input().split(" ")))
    values=[]
    for j in range(n):
        h,m=list(map(int,input().split(" ")))
        if((H>h)|((H==h)&(M>m))):
            pslept=(24*60)-(H*60+M)+(h*60+m)
        else:
            pslept=abs((H*60+M)-(h*60+m))
        values.append(pslept)
    minimum=min(values)
    result.append(minimum)
for i in result:
    print(i//60,i%60)
    

