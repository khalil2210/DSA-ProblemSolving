n=int(input())
t=[]
for i in range(n):
    ch=input()
    if(len(ch)>10):
        ln=len(ch)
        new=ch[0]+str(len(ch[1:ln-1]))+ch[-1]
        t.append(new)
    else:
        t.append(ch)
for i in t:
    print(i)
