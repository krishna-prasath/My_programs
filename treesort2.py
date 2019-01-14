#a=[-1,150,190,170,-1,-1,160,180]
a=[8,7,6,5,4,3]
r=0
for i in range(len(a)-1):
        if a[i]==-1:
            continue
        elif a[i]<=a[i+1]:
            r=a[i]
            a[i]=a[i+1]
            a[i+1]=r

print(a)
