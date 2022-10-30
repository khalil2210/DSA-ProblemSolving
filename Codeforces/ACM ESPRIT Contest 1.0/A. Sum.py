t=int(input())
result=[]
for i in range(t):
    a,b,c=list(map(int,input().split(" ")))
    if((a+b==c)|(a+c==b)|(c+b==a)):
        result.append('YES')
    else:
        result.append('NO')
for i in result:
    print(i)
