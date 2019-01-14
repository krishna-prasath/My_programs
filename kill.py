n=37
x=3
c=bin(n)
c=list(c)
if str(c[-x])=="1":
    c[-x]="0"
a=""
z=a.join(c)
print(int(z,2))
