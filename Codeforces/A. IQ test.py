n=int(input())
t=input().split(" ")
even=0
odd=0
index=0
for i in range(0,3):
    if((int(t[i])%2)==0):
        even+=1
    else:
        odd+=1
if(even>odd):
    for i in range(len(t)):
        if(int(t[i])%2==1):
            index=i
            break
        
else:
    for i in range(len(t)):
        if(int(t[i])%2==0):
            index=i
            break
print(i+1)
