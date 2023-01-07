import math
def isPerfectSquare(n):
    sqrt=math.ceil(math.sqrt(n//2))
    if((sqrt**2)*2==n):
        return True
    return False

t=int(input())
result=[]
for i in range(t):
    n=int(input())
    if(n%2!=0):
        result.append('NO')
    else:
        #check if perfect square
        if((isPerfectSquare(n))|(isPerfectSquare(n//2))):
            result.append('YES')
        else:
            result.append('NO')
for i in result:
    print(i)
