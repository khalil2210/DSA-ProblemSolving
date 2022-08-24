from numpy import *
output=[]
t=int(input(""))
for i in range (t) :
    n,x=input("").split(" ")
    n=int(n)
    x=int(x)
    array=input("").split(" ")
    for i in range(len(array)):
        array[i]=int(array[i])
    matrice=zeros((n,n),int)
    for i in range(n):
        for j in range(i,n):
            matrice[i,j]=sum(array[i:j+1])
    #print(matrice)
    maxm=matrice[0,0]
    for i in range(n):
        for j in range(i,n):
            if(matrice[i,j]>maxm):
                maxm=matrice[i,j]
    #print(maxm)
    t=where(matrice==maxm)
  #  print(t)
    
    
    
    cord=[(t[0][i],t[1][i])for i in range (len(t[0]))]
   # print(cord)
    maxc=max([i[1]for i in cord])+1
    #print(maxc)
    afficher=[]
    if(maxm<=0):
        afficher.append(0)
    else:
        afficher.append(maxm)
   
    for k in range(1,n+1):
        maxcord=[]
        for i in cord :
            if(i[0]-k+1>=0):
                maxcord.append(matrice[i[0]-k+1][i[1]]+k*x)
     #   print(maxcord)
        if(maxcord!=[]):
            if(max(maxcord)>=afficher[k-1]):
                afficher.append(max(maxcord))
            else:
                afficher.append(afficher[k-1])
   
        else:
            
            
            rem=-len(afficher)+maxc
            if(rem>=0):
                afficher.append(afficher[k-1]+x)
                
            else:
                afficher.append(afficher[k-1])
                
    for i in range(len(afficher)):
        afficher[i]=str(afficher[i])
        
    output.append(" ".join(afficher))
for i in output:
    print(i)
    
    
  
    
