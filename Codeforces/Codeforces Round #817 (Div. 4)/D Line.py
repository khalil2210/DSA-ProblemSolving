t=int(input())
result=[]
for i in range(t):
    n=int(input())
    ch=input()
    test=[]
    if(n%2==1):
        optimal='R'*(n//2)+ch[n//2]+'L'*(n//2)
    else:
        optimal='R'*(n//2)+'L'*(n//2)
    sum=0
    for j in range (len(ch)):
        if(ch[j]=='L'):
            sum+=j
        else:
            sum+=n-1-j
    #print(optimal,sum)
    #feha ghalta
    for j in range(len(ch)//2):
        if(ch[j]!=optimal[j]):
            difference=n-1-(2*j)
            sum+=difference
            test.append(str(sum))

        if(ch[n-1-j]!=optimal[n-1-j]):
            difference=(n-1-j)-j
            sum+=difference
            test.append(str(sum))


    h=n-len(test)
    test=test+h*[str(sum)]
    result.append(" ".join(test))
for i in result:
    print(i)



