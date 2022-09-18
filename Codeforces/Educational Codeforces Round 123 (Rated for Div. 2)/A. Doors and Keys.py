t=int(input())
result=[]
for i in range(t):
    ch=input()
    keys=[0,0,0]
    test="Yes"
    for i in ch:
        if(i=='r'):
            keys[0]=1
        elif(i=='g'):
            keys[1]=1
        elif(i=='b'):
            keys[2]=1
        else:
            if((i=='R')&(keys[0]==0)|(i=='G')&(keys[1]==0)|(i=='B')&(keys[2]==0)):
                test="NO"
    result.append(test)
for i in result :
    print(i)
