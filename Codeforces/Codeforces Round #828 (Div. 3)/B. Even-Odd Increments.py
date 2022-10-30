t=int(input())
result=[]
for i in range(t):
    n,q=list(map(int,input().split(" ")))
    ai=list(map(int,input().split(" ")))
    sum,nbp,nbi=0,0,0
    for j in ai:
        if(j%2==0):
            nbp+=1
        else:
            nbi+=1
        sum+=j
    for j in range(q):
        type,xj=list(map(int,input().split(" ")))
        if((type==0)&(xj%2==1)):
            sum+=nbp*xj
            nbi+=nbp
            nbp=0

        elif((type==0)&(xj%2==0)):
            sum+=nbp*xj


        elif((type==1)&(xj%2==1)):
            sum+=nbi*xj
            nbp+=nbi
            nbi=0

        else:
            sum+=nbi*xj
        result.append(sum)

for i in result:
    print(i)
