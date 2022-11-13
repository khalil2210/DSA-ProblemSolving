def saveTheMagazines(tab,indexes,a1,j,n):
    j+=1
    sum=0
    min=tab[j]
    for i in range(j,n):
        if(indexes[i]=='0'):
            return [i,max(sum+a1-min,sum)]
        else:
            sum+=tab[i]
            if(min>tab[i]):
                min=tab[i]
    return [n,max(sum+a1-min,sum)]


t=int(input())
result=[]
for i in range(t):
    n=int(input())
    indexes=list(input())
    tab=list(map(int,input().split(' ')))
    sum=0
    j=0
    if((n==1)&(indexes[0]=='1')):
        result.append(tab[0])
    else:
        while(j<n-1):
            if((indexes[j]=='0')&(indexes[j+1]=='1')):
                res=saveTheMagazines(tab,indexes,tab[j],j,n)
                j=res[0]
                sum+=res[1]
            elif(indexes[j]=='1'):
                sum+=tab[j]
                j+=1
            else:
                j+=1
        if((j==n-1)&(indexes[-1]=='1')):
            sum+=tab[-1]
        result.append(sum)
for i in result:
    print(i)

