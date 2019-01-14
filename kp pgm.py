a=[0,1,2,-1,3,-2,4,0,0,2]
c=0
d=0
e=0
f=0
g=0
h=0
k=0
for i in range(len(a)):
    if a[i]>0:
        f+=a[i]
        c=c+1
    elif a[i]<0:
        g+=a[i]
        d=d+1
    else:
        e=e+1
for i in range(len(a)//2):
    h+=a[i]
for i in range(len(a)//2,len(a)):
    k+=a[i]
print(c,d,e)
print(f,g)
print(h,k)
