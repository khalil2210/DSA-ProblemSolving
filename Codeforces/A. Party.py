def checkchild(a,i):
    value=0
    while(a[i]!=-1):
        value+=1
        i=a[i]
    return value

n=int(input())
index=[0]
sum=0
for i in range(n):
    pi=int(input())
    index.append(pi)
for i in range(1,n+1):
    test=checkchild(index,i)
    if(sum<test):
        sum=test
print(sum+1)




