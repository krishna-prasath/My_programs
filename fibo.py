#fibo series
a=0
b=1
c=0
z=int(input("enter the limit"))
print(a)
print(b)
for i in range(z-2):
    c=a+b
    a=b
    b=c
    print(c)
    
    
