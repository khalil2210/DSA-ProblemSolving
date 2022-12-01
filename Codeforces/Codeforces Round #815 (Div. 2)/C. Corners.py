def checkConnectedZero(a,b,c,d):
    t=[a,b,c,d]
    count=t.count('0')
    if(count>1):
        return True
    return False


t=int( input())
result=[]
for i in range(t):
    n,m=list(map(int,input().split(" ")))
    ligne=[]
    for l in range(n):
        ligne.append(list(input()))
    nbones=0
    conn=False
    for l in range(n-1):
        nbones+=ligne[l].count('1')
        for c in range(m-1):
            if(checkConnectedZero(ligne[l][c],ligne[l][c+1],ligne[l+1][c],ligne[l+1][c+1])==True):
                conn=True
    nbones+=ligne[-1].count('1')
    if(nbones==0):
        result.append(0)
    elif(nbones==n*m):
        result.append(nbones-2)
    elif(conn==False):
        result.append(nbones-1)
    else:
        result.append(nbones)
for i in result:
    print(i)
