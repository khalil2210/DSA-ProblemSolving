t=int(input())
result=[]
for i in range(t):
    n=int(input())
    tab=list(map(int,input().split(" ")))
    tab.sort()
    h=True
    for j in range(n-1):
        if(tab[j+1]<=tab[j]):
            h=False
            break
    if(h==True):
        print('YES')
    else:
        print('NO')
for i in result:
    print(i)
