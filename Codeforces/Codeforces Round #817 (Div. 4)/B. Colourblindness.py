t=int(input())
result=[]
for i in range(t):
    iden='YES'
    n=int(input())
    row1=input()
    row2=input()
    for j in range(n):
        if(row1[j]!=row2[j]):
            if not(((row1[j]=='B')|(row1[j]=='G'))&(((row2[j]=='B')|(row2[j]=='G')))):
                iden='NO'
    result.append(iden)
for i in result:
    print(i)
            
    
