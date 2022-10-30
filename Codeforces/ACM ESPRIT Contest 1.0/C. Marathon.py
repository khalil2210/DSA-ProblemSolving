t=int(input())
result=[]
for i in range(t):
    sum=0
    a,b,c,d=list(map(int,input().split(" ")))
    if(b>a):
        sum+=1
    if(c>a):
        sum+=1
    if(d>a):
        sum+=1
    result.append(sum)
for i in result:
    print(i)
