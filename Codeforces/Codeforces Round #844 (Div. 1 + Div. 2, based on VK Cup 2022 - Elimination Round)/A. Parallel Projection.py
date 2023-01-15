t=int(input())
result=[]
for i in range(t):
    w,d,h=list(map(int,input().split(" ")))
    a,b,f,g=list(map(int,input().split(" ")))
    case1=abs(a-f)+min(b+g,d-b+d-g)
    case2=abs(b-g)+min(a+f,w-a+w-f)
    result.append(min(case1,case2)+h)
for i in result:
    print(i)
