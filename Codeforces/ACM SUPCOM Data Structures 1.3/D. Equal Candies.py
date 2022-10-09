t=int(input())
result=[]
for i in range(t):
    n=int(input())
    ai=list(map(int,input().split(" ")))
    minimum=min(ai)
    sum=0
    for j in ai:
        sum+=j-minimum
    result.append(sum)
for i in result:
    print(i)

