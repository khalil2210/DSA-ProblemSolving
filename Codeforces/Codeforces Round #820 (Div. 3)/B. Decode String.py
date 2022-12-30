q=int(input())
result=[]
alphabets=[chr(i+97) for i in range(26)]
for i in range(q):
    n=int(input())
    code=input()
    j=n-1
    ch=''
    while(j>=0):
        if(code[j]!='0'):
            ch+=alphabets[int(code[j])-1]
            j-=1
        else:
            ch+=alphabets[int(code[j-2:j])-1]
            j-=3

    result.append(ch[::-1])
for i in result:
    print(i)
