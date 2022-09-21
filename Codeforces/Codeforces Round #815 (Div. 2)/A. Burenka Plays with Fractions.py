t=int(input())
result=[]
for i in range(t):

    a,b,c,d=list(map(int,input().split(" ")))
    if((a==0)|(c==0)):
        if((a==0)&(c!=0)):
            result.append(1)
        elif((c==0)&(a!=0)):
            result.append(1)
        else:
            result.append(0)
    elif(a*d==b*c):
        result.append(0)
    else:
        if(((a*d)%(c*b)==0)|((c*b)%(a*d)==0)):
            result.append((1))
        else:
            result.append(2)

for i in result :
    print(i)



