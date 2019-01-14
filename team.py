a=[50,60,60,45,70]
s=[]
b,b1=0,0
for i in range(len(a)):
    if i%2==0:
        b=b+a[i]
    else:
        b1=b1+a[i]
s.append(b)
s.append(b1)

print(s)
