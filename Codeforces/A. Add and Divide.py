t=int(input())
result=[]
for i in range(t):
    j=0
    a,b=list(map(int,input().split(" ")))
    minimum=float('inf')
    initialea=a
    if(b==1):
        count=[minimum]
        j=1
    else:
        count=[]
    while(j<=minimum-1):
        a=initialea
        countt=j
        while((a//(j+b))!=0):
            countt+=1
            a=a//(j+b)
        countt+=1
        if(countt<minimum):
            minimum=countt
            #print(minimum)
        count.append(minimum)
        j+=1
    result.append(minimum)

for i in result:
    print(i)

