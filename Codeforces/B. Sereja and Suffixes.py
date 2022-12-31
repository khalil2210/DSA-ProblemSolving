n,m=list(map(int,input().split(" ")))
tab=list(map(int,input().split(" ")))
numbers=[0 for i in range ((10**5)+1)]
distinct=[]
d=0
result=[]
for i in range(n-1,-1,-1):
    if(numbers[tab[i]]==0):
        numbers[tab[i]]+=1
        d+=1
    distinct.append(d)
distinct.reverse()
for i in range(m):
    li=int(input())
    result.append(distinct[li-1])
for i in result:
    print(i)





