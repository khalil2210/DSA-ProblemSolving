t=int(input())
result=[]
for i in range(t):
    n,c=list(map(int,input().split(" ")))
    countt=[0 for i in range(101)]
    orbit=input().split(" ")
    sum=0
    for j in orbit:
        countt[int(j)]=countt[int(j)]+1
    for j in countt:
        sum+=min(j,c)
    result.append(sum)
for i in result:
    print(i)

