t=int(input())
result=[]
for i in range(t):
    n=int(input())
    tab=list(map(int,input().split(" ")))
    indfirstzero,indlastone=-1,-1
    zero,one,inv=0,0,0
    ref=[]
    for j in range(n):
        if(tab[j]==0):
            inv+=one
        ref.append([zero,one,inv])
        if(tab[j]==1):
            indlastone=j
        elif((tab[j]==0)&(indfirstzero==-1)):
            indfirstzero=j
        if(tab[j]==0):
            zero+=1
        if(tab[j]==1):
            one+=1
    if((indfirstzero==-1)|(indlastone==-1)):
        result.append(n-1)
    else:
        #conition ne9sa
        if(indlastone!=n-1):
            lc=inv-(ref[-1][0]-ref[indlastone][0]+1)+ref[indlastone][1]
        else:
            lc=inv+ref[indlastone][1]
        if(tab[-1]==0):
            fc=inv-ref[indfirstzero][2]+ref[-1][0]
        else:
            fc=inv-ref[indfirstzero][2]+ref[-1][0]-1
        result.append(max(inv,lc,fc))
for i in result:
    print(i)




