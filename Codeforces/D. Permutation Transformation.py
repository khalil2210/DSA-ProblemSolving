def permut(tab,tab1,l,r,s):   
    if(r<l):
        return ([],s)
    if((len(tab[l:r+1])==1)):
        return ([tab.index(tab1[l:r+1][0])],s)
    indexmaximum=tab.index(max(tab1[l:r+1]))
    tab1[indexmaximum]=s
    s+=1
    left=permut(tab,tab1,l,indexmaximum-1,s)
    if(left[0]!=[]):
        tab1[left[0][0]]=left[1]
    right=permut(tab,tab1,indexmaximum+1,r,s)
    if(right[0]!=[]):
        tab1[right[0][0]]=right[1]
    return([],s)
n=int(input())
for i in range(n):
    ln=int(input())
    tab=list(map(int,input().split(" ")))
    s=0
    tab1=tab.copy()
    if(len(tab)==1):
        print(0)
    else:
        
        permut(tab,tab1,0,len(tab)-1,s)
        tab1=list(map(str,tab1))
        print(" ".join(tab1))
    
