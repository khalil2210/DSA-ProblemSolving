t=int(input())
result=[]
for i in range(t):
    x=int(input())
    count=0
    tab=list(map(int,input().split(" ")))
    while(tab[x-1]!=0):
        count+=1
        x=tab[x-1]
        
    if(count==2):
        result.append("YES")
    else:
        result.append("NO")
        
for i in result:
    print(i)
