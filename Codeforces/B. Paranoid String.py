t=int(input())
result=[]
for i in range(t):
    n=int(input())
    s=input()
    nbpairs=n
    for j in range(1,n):
        if(s[j]!=s[j-1]):
            nbpairs+=j
    result.append(nbpairs)
for i in result:
    print(i)
