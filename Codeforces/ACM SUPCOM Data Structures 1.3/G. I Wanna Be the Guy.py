n=int(input())
final=[]
h=True
for i in range(2):
    tab=input()
    ai=tab[1:]
    final.append(ai)
for i in range(1,n+1):
    if((str(i) not in final[0])&(str(i) not in final[1])):
        h=False
        print("Oh, my keyboard!")
        break
if(h==True):
    print("I become the guy.")

