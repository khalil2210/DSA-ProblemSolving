n,m=list(map(int,input().split(" ")))
count=0
while(m>n):
    if(m%2!=0):
        m=(m+1)//2
        count+=1
    else:
        m=m//2
    count+=1
print(n-m+count)
