t=int(input())
result=[]
for i in range(t):
    n=int(input())
    d={}
    tab=list(map(int,input().split(" ")))
    c=0
    for i in tab:
        if(i not in d):
            c+=1
            d[i]=1
        if(c==3):
            result.append(n)
            break
    if(c<=2):
        result.append((n//2)+1)
for i in result:
    print(i)

