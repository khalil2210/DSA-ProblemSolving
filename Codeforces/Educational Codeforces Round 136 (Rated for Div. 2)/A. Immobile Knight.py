t=int(input())
result=[]
for b in range(t):
    n,m=list(map(int,input().split(" ")))
    isolatedcell=""
    for i in range(1,n+1):
        for j in range(1,m+1):
          #  print(i,j,((i+1<=n)&((1<=j-2<=m)|(j+2<=m))),((i+2<=n)&((1<=j-1<=m)|(j+1<=m))),((1<=i-1<=n)&((1<=j-2<=m)|(j+2<=m))),(1<=i-2<=n)&((1<=j-1<=m)|(j+1<=m)))

            if(not(((i+2<=n)&((1<=j-1<=m)|(j+1<=m)))|((i+1<=n)&((1<=j-2<=m)|(j+2<=m)))|
                   ((1<=i-2<=n)&((1<=j-1<=m)|(j+1<=m)))|((1<=i-1<=n)&((1<=j-2<=m)|(j+2<=m))))):
                isolatedcell=str(i)+" "+str(j)
    if(isolatedcell == ""):
        result.append(str(n)+" "+str(m))
    else:
        result.append(isolatedcell)

for i in result:
    print(i)
