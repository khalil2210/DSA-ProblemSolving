n,a,b=list(map(int,input().split(" ")))
result=(a+b)%n
if(result==0):
    print(a+(b%n))
else:
    print(result)
