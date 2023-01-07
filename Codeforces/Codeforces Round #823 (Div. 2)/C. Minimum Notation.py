t=int(input())
result=[]
for i in range(t):
    s=input()
    n=len(s)
    FIFO=[['9',-1]]
    indiceMin=FIFO[0][1]
    Minimum=FIFO[0][0]
    for j in range(n-1,-1,-1):
        if(s[j]<=Minimum):
            Minimum=s[j]
            indiceMin=j
            FIFO.insert(0,[Minimum,indiceMin])
    if(Minimum=='9'):
        result.append(s)
    else:
        d={'0':-1,'1':-1,'2':-1,'3':-1,'4':-1,'5':-1,'6':-1,'7':-1,'8':-1,'9':-1}
        for j in range(n):
            if(j==indiceMin):
                del(FIFO[0])
                indiceMin=FIFO[0][1]
                Minimum=FIFO[0][0]
            if((s[j]>Minimum)&(j<indiceMin)&(s[j]!='9')):
                sjPlusOne=str(int(s[j])+1)
                if(d[sjPlusOne]==-1):
                    d[sjPlusOne]=1
                else:
                    d[sjPlusOne]+=1
            else:
                if(d[s[j]]==-1):
                    d[s[j]]=1
                else:
                    d[s[j]]+=1
        ch=""
        l=[i for i in d.keys() if d[i]!=-1]
        for c in l:
            ch+=c*d[c]
        result.append(ch)
for i in result:
    print(i)
