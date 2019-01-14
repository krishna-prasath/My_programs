a1=[-1,-1]
a=[]
a2=[]
for i in range(len(a1)):
    if a1[i]==-1:
        a.append(i)
    else:
        a2.append(a1[i])
a2.sort()
for i in range(len(a)):
    a2.insert(a[i],-1)

print(a2)
