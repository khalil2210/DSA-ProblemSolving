t=int(input())
result=[]
for i in range(t):
    n=int(input())
    tab=list(map(int,input().split(" ")))
    valleys=0
    if(n==1):
        result.append('YES')
        continue
    l,r=0,0
    while(r<n):
        if((r==n-1)):
            if(l==0):
                valleys+=1
            elif(tab[l-1]>tab[l]):
                valleys+=1
            break
        if((l==0)&(tab[r+1]>tab[r])):
            valleys+=1
        elif(l!=0):
            if((tab[r+1]>tab[r])&((tab[l-1]>tab[l]))):
                valleys+=1
        if(tab[r+1]==tab[r]):
            r+=1
        elif(tab[r+1]!=tab[l]):
            r+=1
            l=r
    if(valleys==1):
        result.append('YES')
    else:
        result.append('NO')

for i in result:
    print(i)


