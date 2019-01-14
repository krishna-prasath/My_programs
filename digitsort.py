a=[12,9,1,3]
a1=[12,9,1,3]
s=[]
z=0
c=0
#expected a=[1,3,12,9]
for i in range(len(a)):
    q=0
    while(a1[i]>0):
        z=a1[i]%10
        q=q+z
        a1[i]=a1[i]//10
    s.append(q)
print(a)    
s.sort()                
print(s)
