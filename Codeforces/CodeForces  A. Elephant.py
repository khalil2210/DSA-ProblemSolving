x=int(input())
step=0
while(x>5):
    step=x//5
    x=x%5
if(x!=0):
    step+=1
print(step)
