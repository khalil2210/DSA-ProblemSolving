n=int(input())
tab=list(map(int,input().split(" ")))
i=n
result=[]
result.append(str(i))
while(1):
    result.append(str(tab[i-2]))
    i=tab[i-2]
    if(i==1):
        break
print(" ".join(result[::-1]))
    
