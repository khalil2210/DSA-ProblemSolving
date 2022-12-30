def ordonner(a):
    return ord(a)-96
t=int(input())
result=[]
for i in range(t):
    s=input()
    n=len(s)
    indices=[[]for j in range(26)]
    Lindexes=list(map(ordonner,s))
    interm=Lindexes[1:-1]
    for j in range(n-2):
        indices[interm[j]-1].append(str(j+2))
    interm.sort()
    if(Lindexes[0]>Lindexes[-1]):
        interm.reverse()
    visitedTiles=['1']
    start,end=min(Lindexes[0],Lindexes[-1]),max(Lindexes[0],Lindexes[-1])
    for j in interm:
        if(start<=j<=end):
            visitedTiles+=indices[j-1]
            indices[j-1]=[]
    cost=abs(Lindexes[0]-Lindexes[-1])
    visitedTiles.append(str(n))
    result.append(str(cost)+" "+str(len(visitedTiles)))
    result.append(" ".join(visitedTiles))
for i in result:
    print(i)
