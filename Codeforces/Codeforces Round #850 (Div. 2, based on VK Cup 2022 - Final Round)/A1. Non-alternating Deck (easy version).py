t=int(input())
result=[]
for i in range(t):
    n=int(input())
    alice=1
    alicewhite=1
    aliceblack=0
    Bob=0
    bobwhite=0
    bobblack=0
    n-=1
    bobTour=1
    if(n==1):
        Bob+=1
        bobblack+=1
    for j in range(2,n+1,2):
        if(bobTour):
            if(n-j>=0):
                Bob+=j
                addedwhite=j//2
                bobwhite+=addedwhite
                bobblack+=(j-addedwhite)
                n-=j
            if(n-(j+1)>=0):
                Bob+=j+1
                n-=(j+1)
                addedwhite=(j+1)//2
                bobwhite+=addedwhite
                bobblack+=((j+1)-addedwhite)
            else:
                Bob+=n
                addedwhite=n//2
                bobwhite+=addedwhite
                bobblack+=(n-addedwhite)
                break
        else:
            if(n-j>=0):
                alice+=j
                n-=j
                addedwhite=j//2
                alicewhite+=addedwhite
                aliceblack+=(j-addedwhite)
            if(n-(j+1)>=0):
                alice+=j+1
                n-=(j+1)
                addedwhite=((j+1)//2)+1
                alicewhite+=addedwhite
                aliceblack+=((j+1)-addedwhite)
            else:
                alice+=n
                if(n%2==0):
                    addedwhite=(n)//2
                else:
                    addedwhite=(n//2)+1
                alicewhite+=addedwhite
                aliceblack+=(n-addedwhite)
                break
        bobTour=1-bobTour
    result.append(str(alicewhite)+" "+str(aliceblack)+" "+str(bobwhite)+" "+str(bobblack))
for i in result:
    print(i)