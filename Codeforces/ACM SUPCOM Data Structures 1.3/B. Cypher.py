t=int(input())
result=[]
for i in range(t):
    n=int(input())
    ai=list(map(int,input().split(" ")))
    ch=""
    for j in range(n):
        b,s=input().split(" ")
        difference=s.count("D")-s.count("U")
        if(difference>0):
            ai[j]=(ai[j]+difference)%10
        elif(ai[j]+difference>=0):
            ai[j]=ai[j]+difference
        else:
            ai[j]=10+(ai[j]+difference)





        ch+=str(ai[j])+" "
    result.append(ch)
for i in result:
    print(i)










