t=int(input())
result=[]
for i in range(t):
    n=int(input())
    a=list(map(int,input().split(" ")))
    b=list(map(int,input().split(" ")))
    resultt=0
    for j in range(n):
        if(a[j]!=b[j]):
            resultt+=1
    numberdiff=abs(a.count(1)-b.count(1))
    if(resultt==numberdiff):
        result.append(resultt)
    else:
        result.append(numberdiff+1)
for i in result:
    print(i)



