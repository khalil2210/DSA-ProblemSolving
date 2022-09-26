t=int(input())
result=[]
for i in range (t):
    n=int(input())
    tab=input().split(" ")
    d={}
    for j in tab:
        if(j not in d):
            d[j]=1
        else:
            d[j]=d[j]+1

    itemremoved=0
    for j in range(n):
        #print(d)
        if(d[tab[j]]!=1):
            d[tab[j]]=d[tab[j]]-1
            itemremoved=j+1

    result.append(itemremoved)





for i in result :
    print(i)
    
    

