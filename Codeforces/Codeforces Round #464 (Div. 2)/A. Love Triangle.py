n=int(input())
tab=list(map(int,input().split(" ")))
i=0
result="NO"
while(i<len(tab)):
    a=tab[i]
    b=tab[a-1]
    if(tab[b-1]-1==i):
        result="YES"
        break
    i+=1
print(result)
