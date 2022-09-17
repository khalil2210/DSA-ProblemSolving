t=int(input())
result=[]
name=['T','i','m','u','r']
name.sort()
for i in range(t):
    n = int(input())
    s = input()
    if( len(s) !=5 ):
        result.append("NO")
    else:
        s=list(s)
        s.sort()
        if(s!=name):
            result.append("NO")
        else:
            result.append("YES")

for i in result:
    print(i)
    
