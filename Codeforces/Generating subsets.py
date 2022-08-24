nums=[1,2,3,4,5,7,8,5,2,2]
n=len(nums)
output=[[]]

for i in range(n):
    tabs=[0 for j in range(n)]
    indice=0
    tabs[i]=1
    output.append([nums[i]])
    for j in range((2**i)-1):
        
        if((tabs[indice]==0)&(tabs[indice+1]==1)):
            tabs[indice]=1
            indice=0
        elif((tabs[indice]==1)&(tabs[indice+1]==0)):
            tabs[indice]=0
            tabs[indice+1]=1
        elif((tabs[indice]==0)&(tabs[indice+1]==0)):
            tabs[indice]=1
        elif((tabs[indice]==1)&(tabs[indice+1]==1)):
            while(tabs[indice]==1):
                tabs[indice]=0
                indice=indice+1
            tabs[indice]=1
            indice=0
        tabj=[]
        for k in range(n):
             if(tabs[k]==1):
                    tabj.append(nums[k])
        output.append(tabj) 


    
print(output)   
