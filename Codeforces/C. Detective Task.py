t=int(input())
result=[]
for i in range(t):
    s=input()
    n=len(s)
    indiceFirstZero=n-1
    indiceLastOne=0
    zeroFound=False
    for j in range(n):
        if((s[j]=='0')&(zeroFound==False)):
            indiceFirstZero=j
            zeroFound=True
        elif(s[j]=='1'):
            indiceLastOne=j
    result.append(len(s[indiceLastOne:indiceFirstZero+1]))
for i in result:
    print(i)
