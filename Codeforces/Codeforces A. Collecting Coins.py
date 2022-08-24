n=int(input())
result=[]
for i in range(n):
    a,b,c,n=list(map(int,input().split(" ")))
    summ=a+b+c+n
    if(n==0):
        if(a==b==c):
            result.append("YES")
        else:
            result.append("NO")
    elif(summ%3==0):
        A=(summ/3)-a
        B=(summ/3)-b
        C=(summ/3)-c
        if(((A>=0)&(B>=0)&(C>=0))&(A+B+C==n)):
            result.append("YES")
        else:
            result.append("NO")
    else:
        result.append("NO")
for i in result:
    print(i)



