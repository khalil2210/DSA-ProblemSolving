t=int(input())
result=[]
for l in range(t):
    n=int(input())
    ai=list(map(int,input().split(" ")))
    bi=list(map(int,input().split(" ")))
    k=0
    impos=False
    moves=[]
    for i in range(n):
        minai,minbi=ai[i],bi[i]
        swapIndice=i
        for j in range(i,n):
            if((ai[j]<=minai)&((bi[j]<=minbi))):
                minai,minbi=ai[j],bi[j]
                swapIndice=j
        if(swapIndice!=i):
            k+=1
            moves.append(str(i+1)+" "+str(swapIndice+1))
            ai[i],ai[swapIndice]=ai[swapIndice],ai[i]
            bi[i],bi[swapIndice]=bi[swapIndice],bi[i]
    for i in range(n-1):
        if((ai[i]>ai[i+1])|(bi[i]>bi[i+1])):
            impos=True
    if(impos==False):
        result.append(k)
        result+=moves
    else:
        result.append(-1)
for i in result:
    print(i)





