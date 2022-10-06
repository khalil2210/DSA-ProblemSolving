t=int(input())
result=[]
for i in range(t):
    n=int(input())
    tab=list(map(int,input().split(" ")))
    sett=set()
    distinct=[]
    d={0:0}
    for j in tab:
        sett.add(j)
        distinct.append(len(sett))
        if(j not in d):
            d[j]=1
        else:
            d[j]+=1
    ini=len(result)
    for j in range(n-1,0,-1):
        if(tab[j-1]==tab[j]):
            d[tab[j]]-=1
        elif(((tab[j-1]>tab[j])&(d[tab[j]]>1))|((tab[j-1]<tab[j])&(d[tab[j]]>1))):
            result.append(distinct[j])
            break
        elif((tab[j-1]>tab[j])&(d[tab[j]]==1)):
            result.append(distinct[j]-1)
            break
    if(ini==len(result)):
        result.append(0)
for i in result:
    print(i)
