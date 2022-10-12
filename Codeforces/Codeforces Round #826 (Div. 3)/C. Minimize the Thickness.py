def twoPointers(array,check,n):
    i,j=0,0
    result=[]
    sum=0
    while(j<n):
        sum+=array[j]
        if(sum>check):
            return -1
        elif(sum==check):
            result.append(j-i+1)
            i=j+1
            j=i
            sum=0
        else:
            j+=1
    if(sum==0):
        return max(result)
    else:
        return -1





















t=int(input())
result=[]
for i in range(t):
    n=int(input())
    array=list(map(int,input().split(" ")))
    Sum=sum(array)
    prresult=[]
    for j in range(n,0,-1):
        if(Sum%j==0):
            a=twoPointers(array,Sum//j,n)
            if(a!=-1):
                prresult.append(a)
    result.append(min(prresult))
for i in result:
    print(i)





