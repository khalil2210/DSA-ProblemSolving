t=int(input())
result=[]
for i in range (t):
    s=int(input())
    if(s<10):
        
        result.append(s)
    else:
        subs=9
        chaine=''
        while(s!=0):
            if(s-subs>=0):
                s-=subs
                chaine=str(subs)+chaine
                subs-=1
            else:
                subs-=1
        result.append(chaine)
for i in result:
    print(i)

