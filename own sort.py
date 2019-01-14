# new and own sorting method
a=[3,2,54,6,3,2,24,67,72]
a1=[]
r=0
for i in range(len(a)):
    print(len(a))
    r=min(a)
    a1.append(r)
    a.remove(r)
    
    
print(a1)
