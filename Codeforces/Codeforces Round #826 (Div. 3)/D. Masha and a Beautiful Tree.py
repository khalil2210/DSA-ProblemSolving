sum=0
def sort(l,r):
    global sum
    if((l[-1]>r[0])&(r[-1]<l[0])):
        sum+=1
        return r+l
    elif(l[-1]<r[0]):
        return l+r
    else :
        return None

def divide(array,m):
    if(m==1):
        return array
    else:
        l=divide(array[:m//2],m//2)
        r=divide(array[m//2:],m//2)
    if((l==None)|(r==None)):
        return None
    else:
        return sort(l,r)



t=int(input())
result=[]
for i in range(t):
    sum=0
    m=int(input())
    p=list(map(int,input().split(" ")))
    if(divide(p,m)==None):
        result.append(-1)
    else:
        result.append(sum)

for i in result:
    print(i)
