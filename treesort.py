a=[-1,150,190,170,-1,-1,160,180]
#a=[8,7,6,5,4,3]
r=0
sum1=0
for i in range(len(a)):
    for j in range(len(a)-i-1):
        if a[j]!=-1 and a[j+1]!=-1:
            break
        else:
            r=a[j]
            a[j]=a[j+1]
            a[j+1]=r
    
for i in range(len(a)):
    for j in range(len(a)-i-1):
        if a[j]>=a[j+1] and a[j+1]!=-1:
            r=a[j]
            a[j]=a[j+1]
            a[j+1]=r
print(a)
