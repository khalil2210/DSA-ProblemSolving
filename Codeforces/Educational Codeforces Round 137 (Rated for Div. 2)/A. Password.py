import math
t=int(input())
result=[]
for i in range(t):
    n=int(input())
    tab=list(map(int,input().split(' ')))
    result.append(math.comb(10-n,2)*math.comb(4,2))
for i in result:
    print(i)

