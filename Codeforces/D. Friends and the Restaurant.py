t=int(input())
result=[]
for i in range(t):
    bill=[]
    n=int(input())
    xi=list(map(int,input().split(" ")))
    yi=list(map(int,input().split(" ")))
    for j in range(n):
        bill.append(yi[j]-xi[j])
    bill.sort()
    start,end=0,n-1
    sum=0
    while(start<end):
        if(bill[end]+bill[start]>=0):
            end-=1
            sum+=1
        start+=1
    result.append(sum)
for i in result:
    print(i)
