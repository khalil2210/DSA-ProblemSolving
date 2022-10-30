t=int(input())
result=[]
for i in range(t):
    ch=input()
    sum1=0
    sum2=0
    for i in range(3):
        sum1+=int(ch[i])
    for i in range(3,len(ch)):
        sum2+=int(ch[i])
    if(sum1==sum2):
        result.append('YES')
    else:
        result.append('NO')
for i in result:
    print(i)
