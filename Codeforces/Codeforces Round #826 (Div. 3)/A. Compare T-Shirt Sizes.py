t=int(input())
result=[]
for i in range(t):
    a,b=input().split(" ")
    if(a[-1]==b[-1]):
        if(a[-1]=='S'):
            if(len(a)>len(b)):
                result.append('<')
            elif(len(a)<len(b)):
                result.append('>')
            else:
                result.append('=')
        elif(a[-1]=='L'):
            if(len(a)>len(b)):
                result.append('>')
            elif(len(a)<len(b)):
                result.append('<')
            else:
                result.append('=')
        else:
            result.append('=')
    elif(a[-1]=='L'):
        result.append('>')
    elif((a[-1]=='M')&(b[-1]=='S')):
        result.append('>')
    else:
        result.append('<')
for i in result:
    print(i)
