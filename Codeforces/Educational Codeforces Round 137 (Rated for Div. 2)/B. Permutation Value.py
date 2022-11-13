t=int(input())
result=[]
for i in range(t):
    n=int(input())
    ch='1 '
    for j in range(3,n+1):
        ch+=str(j)+' '
    ch+='2'
    result.append(ch)
for i in result:
    print(i)
