t=int(input())
result=[]
for i in range(t):
    rating=int(input())
    if(rating>=1900):
        result.append('Division 1')
    elif(1600<=rating<=1899):
        result.append('Division 2')
    elif(1400<=rating<=1599):
        result.append('Division 3')
    else:
        result.append('Division 4')
for i in result:
    print(i)
