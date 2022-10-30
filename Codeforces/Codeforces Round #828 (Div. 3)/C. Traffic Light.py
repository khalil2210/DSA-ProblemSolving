t=int(input())
result=[]
for i in range(t):
    n,c=input().split(' ')
    n=int(n)
    s=input()
    s=s*2
    n=n*2
    indexg=[a for a in range(n) if(s[a]=='g')]
    index=0
    lenindexg=len(indexg)
    max=0
    for j in range(n):
        if((s[j]=='g')&(index+1<lenindexg)):
            index+=1
        elif((s[j]==c)&(max<indexg[index]-j)):
            max=indexg[index]-j
    result.append(max)
for i in result:
    print(i)



