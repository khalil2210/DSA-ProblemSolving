t=int(input())
result=[]
for i in range(t):
    n=int(input())
    s=input()
    alphabets=[0 for j in range(26)]
    sum=0
    for j in s:
        if(alphabets[ord(j)-65]==0):
            alphabets[ord(j)-65]=1
            sum+=1
        sum+=1
    result.append(sum)
for i in result:
    print(i)
