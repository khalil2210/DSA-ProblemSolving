t=int(input())
result=[]
for i in range(t):
    n=int(input())
    enemy=list(map(int,input()))
    pawn=list(map(int,input()))
    count=0
    for i in range(len(pawn)) :
        if(pawn[i]!=0):
            if(enemy[i]==0):
                enemy[i]=2
                count+=1
            elif(i==0):
                if(enemy[i+1]==1):
                    count+=1
                    enemy[i+1]=2                
            elif(i==n-1):
                if(enemy[i-1]==1):
                    count+=1
                    enemy[i-1]=2 
            elif((enemy[i+1]==1)|(enemy[i-1]==1)):
                if(enemy[i-1]==1):
                    count+=1
                    enemy[i-1]=2                
                elif(enemy[i+1]==1):
                    count+=1
                    enemy[i+1]=2  

    result.append(count)
for i in result:
    print(i)
