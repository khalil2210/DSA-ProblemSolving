t=int(input())
result=[]
for i in range(t):
    n=int(input())
    if(n<10):
        result.append(n)
    else:
        length=len(str(n))
        compareTo=int('1'*length)
        result.append(9*(length-1)+(n//compareTo))
for i in result:
    print(i)
