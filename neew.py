n=2468109865423123
a=str(n)
b=list(a)
c=[]  
for i in range(0,len(b)):
    if int(b[i])%2==0:
        c.append(b[i])
c=int("".join(map(str,c)))
print(c)
