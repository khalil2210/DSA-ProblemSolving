t=int(input())
result=[]
for i in range(t):
    n=int(input())
    if(n==3):
        result.append("3 2 1")
        result.append("3 1 2")
        result.append("1 3 2")
    else:
        array=[str(j) for j in range(n,0,-1)]
        result.append(" ".join(array))
        for j in range(n-1):
            array.insert(0,array[n-1])
            del(array[n])
            result.append(" ".join(array))
for i in result:
    print(i)
