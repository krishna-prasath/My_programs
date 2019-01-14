a=145
z=0
x=0
for i in range(len(str(a))):
    z=a%10
    x=x+z
    a=a//10
print(x)
    
