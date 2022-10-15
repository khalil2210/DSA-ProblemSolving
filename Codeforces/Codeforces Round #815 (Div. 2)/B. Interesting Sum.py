t=int(input())
result=[]
for i in range(t):
    n=int(input())
    tab=list(map(int,input().split(" ")))
    maximum1=max(tab)
    minimum1=min(tab)
    tab.remove(maximum1)
    tab.remove(minimum1)
    maximum2=max(tab)
    minimum2=min(tab)
    result.append(maximum1+maximum2-minimum1-minimum2)
for i in result:
    print(i)
