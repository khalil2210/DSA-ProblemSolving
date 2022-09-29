t=int(input())
result=[]
for i in range(t):
    n=int(input())
    if(n%2==0):
        ch=''
        init=1
    else:
        ch='1 '
        init=2
    for j in range(init,n+1,2):
        ch+=str(j+1)+' '+str(j)+' '
    result.append(ch)
for i in result:
    print(i)
