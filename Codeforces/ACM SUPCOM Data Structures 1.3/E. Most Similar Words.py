def sumord(ch1,ch2):
    sum=0
    for i in range(len(ch1)):
        sum+=abs(ord(ch1[i])-ord(ch2[i]))
    return sum
t=int(input())
result=[]
for i in range(t):
    words=[]
    n,m=list(map(int,input().split(" ")))
    for j in range(n):
        words.append(input())
    minimum=sumord(words[0],words[1])
    for j in range(len(words)-1):
        for k in range(j+1,len(words)):
            test=sumord(words[j],words[k])
            if(test<minimum):
                minimum=test
    result.append(minimum)
for i in result:
    print(i)


