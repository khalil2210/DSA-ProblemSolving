def minimum(a,b,c):
    return abs(a-b)+abs(b-c)


t=int(input())
result=[]
for i in range(t):
    n=int(input())
    tab=list(map(int,input().split(" ")))

    tab.sort()
    mini=minimum(tab[0],tab[1],tab[2])
    for j in range(n-2):
        curr=minimum(tab[j],tab[j+1],tab[j+2])
        if(curr<mini):
            mini=curr
    print(mini)



