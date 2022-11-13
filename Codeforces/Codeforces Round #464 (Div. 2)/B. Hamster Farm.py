N,K=list(map(int,input().split(" ")))
boxes=list(map(int,input().split(" ")))
boxnum=1
minbox=N//boxes[0]
hamleft=N%boxes[0]
for i in range(len(boxes)):
    if(N%boxes[i]<hamleft):
        boxnum=i+1
        minbox=N//boxes[i]
        hamleft=N%boxes[i]
print(str(boxnum)+" "+str(minbox))
        
