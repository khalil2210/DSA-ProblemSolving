n =int(input())
res=0
for i in range(n):
    t=input().split(" ")
    for j in range(len(t)):
        t[j]=int(t[j])
    if(sum(t)>=2):
        res+=1
print(res)
