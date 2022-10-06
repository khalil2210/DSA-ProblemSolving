n=int(input())
tab=list(map(int,input().split(" ")))
result=[]
for j in range(n):
    count=[0 for k in range(n)]
    count[j]=1
    if(tab[j]-1==j):
        result.append(str(tab[j]))

    else:
        i=j
        while(1):
            a=tab[i]
            count[a-1]=count[a-1]+1
            if(count[a-1]==2):
                result.append(str(a))
                break
            i=a-1        
print(" ".join(result))
