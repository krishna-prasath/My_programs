n=int(input("enter the number"))
x=[]
a,b=0,1
x.append(a)
x.append(b)
if n==0:
    print(0)
else:
    for i in range(2,n):
        c=a+b
        a=b
        b=c
        x.append(c)
    print(x)
