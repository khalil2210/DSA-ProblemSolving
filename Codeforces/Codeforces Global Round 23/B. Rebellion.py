t=int(input())
result=[]
for i in range(t):
    n=int(input())
    tab=list(map(int,input().split(" ")))
    start,end=0,n-1
    count=0
    while(start<=end):
        if(tab[start]>tab[end]):
            count+=1
            start+=1
            end-=1
        if(tab[start]==0):
            start+=1
        if(tab[end]==1):
            end-=1
    result.append(count)
for i in result:
    print(i)
