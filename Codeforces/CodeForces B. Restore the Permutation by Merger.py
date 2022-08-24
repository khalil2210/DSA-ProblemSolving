t=int(input())
result=[]
for i in range(t):
    n=int(input())
    tab=input().split(" ")
    test=[]
    for j in tab:
        if(j not in test):
            test.append(j)
    result.append(" ".join(test))
for i in result:
    print(i)
