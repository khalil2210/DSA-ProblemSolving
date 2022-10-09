t=int(input())
res=[]
for i in range(t):
    n,k=input().split(" ")
    n=int(n)
    k=int(k)
    
    tab=input().split(" ")
    if((n==1)|(k==n)):
        res.append(0)
    else:
        summ=0
        for j in range(k):
            if(int(tab[j])>k):
                summ+=1
        res.append(summ)
for i in res:
    print(i)
           
                
            
        
