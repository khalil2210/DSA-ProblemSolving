import math
t=int(input())
result=[]
for i in range(t):
    n=int(input())
    result.append(math.ceil(n/2))
for i in result:
    print(i)
