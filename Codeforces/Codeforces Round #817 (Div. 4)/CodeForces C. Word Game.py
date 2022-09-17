t=int(input())
result=[]
for i in range (t):
    n=int(input())
    wordpl1=input().split()
    wordpl2=input().split()
    wordpl3=input().split()
    score1,score2,score3=n*3,0,0
    D={}
    for j in wordpl1:
        D[j]=1
    for j in wordpl2:
        if(j in D):
            score1-=2
            score2+=1
            D[j]+=1
        else:
            score2+=3
            D[j]=1


    for j in wordpl3:
        if(j in D):
            if(D[j]==1):
                score3+=1
                if(j in wordpl1):
                    score1-=2
                else:
                    score2-=2
            else:
                score2-=1
                score1-=1


        else:
            score3+=3

    result.append(str(score1)+" "+str(score2)+" "+str(score3))
for i in result:
    print(i)
