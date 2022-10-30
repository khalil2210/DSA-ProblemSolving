t=int(input())
result=[]
for i in range(t):
    resultc=False
    tabl,tabc=[],[]
    a=input()
    for j in range(8):
        tabl.append(input())
    for j in range(8):
        ch=tabl[0][j]+tabl[1][j]+tabl[2]+tabl[3][j]+tabl[4][j]+tabl[5][j]+tabl[6]+tabl[7][j]
        tabc.append(ch)
    for j in tabl:
        if('.' not in j):
            if(j.count('B')==8):
                result.append('B')
                resultc=True
                break
            elif(j.count('R')==8):
                resultc=True
                result.append('R')
                break
    if(resultc==False):
        for j in tabc:
            if('.' not in j):
                if(j.count('B')==8):
                    result.append('B')
                    break
                elif(j.count('R')==8):
                    result.append('R')
                    break
for i in result:
    print(i)






