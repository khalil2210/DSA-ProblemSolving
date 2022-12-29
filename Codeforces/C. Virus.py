t=int(input())
result=[]
for i in range(t):
    n,m=list(map(int,input().split(" ")))
    ai=list(map(int,input().split(" ")))
    ai.sort()
    nbrBetweenElements=[ai[k+1]-ai[k]-1 for k in range(m-1)]
    nbrBetweenElements.append(n+ai[0]-ai[-1]-1)
    nbrBetweenElements.sort()
    nbrBetweenElements.reverse()
    ind=0
    nbrProtectedH=0
    for ind in range(m):
        if(nbrBetweenElements[ind]-(4*ind)==1):
            nbrProtectedH+=1
            break
        elif(((nbrBetweenElements[ind]-(4*ind)>1))):
            nbrProtectedH+=nbrBetweenElements[ind]-(4*ind)-1
        else:
            break
    result.append(n-nbrProtectedH)
for i in result:
    print(i)
