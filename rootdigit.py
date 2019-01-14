a=[13,20,7,4]
root=[]
a1=0
b1=0
for i in range(len(a)):
    a1=a[i]%10
    b1=a[i]//10
    root.append(a1+b1)
z=root
z.sort()

for i in range(len(a)):
    a1=a[i]%10
    b1=a[i]//10
    if a1+b1!=root[i]:
        print([i])
        
        


print(root)
