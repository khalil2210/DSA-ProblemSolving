t=int(input())
result=[]
for i in range(t):
    n=int(input())
    if(n==2):
        result.append('2 1')
    elif(n==3):
        result.append('-1')
    else:
        ch=''
        if(n%2==1):
            for j in range(n,3,-2):
                ch+=str(j-1)+' '+str(j)+' '
            ch+='1 2 3'
        else:
            for j in range(n,2,-1):
                ch+=str(j)+' '
            ch+='1 2'
        result.append(ch)
for i in result:
    print(i)
