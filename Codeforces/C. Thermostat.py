t=int(input())
result=[]
for i in range(t):
    l,r,p=list(map(int,input().split(" ")))
    a,b=list(map(int,input().split(" ")))
    if(a==b):
        result.append(0)
    elif(a<b):
        if(((a+p)<=b)):
            result.append(1)
        elif(((b+p)<=r)|((a-p)>=l)):
            result.append(2)
        elif((((a+p)<=r)&((b-p)>=l))):
            result.append(3)
        else:
            result.append(-1)
    elif(a>b):
        if(((a-p)>=b)):
            result.append(1)
        elif(((b-p)>=l)|((a+p)<=r)):
            result.append(2)
        elif((((a-p)>=l)&((b+p)<=r))):
            result.append(3)
        else:
            result.append(-1)
for i in result:
    print(i)

