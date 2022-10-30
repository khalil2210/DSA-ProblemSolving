t=int(input())
result=[]
for i in range(t):
    n=int(input())
    tab=list(map(int,input().split(" ")))
    tab.sort()
    h=False
    for j in range(n-2):
        if(tab[j]+tab[j+1]+tab[j+2]==3*tab[j]):
            result.append(tab[j])
            h=True
            break
    if(h==False):
        result.append('-1')
for i in result:
    print(i)
