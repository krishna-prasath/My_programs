a=[8,4,6,2,6,4,7,9,5,8]
a1=[]
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if a[i]==a[j]:
            a1.append(j)
print(a1)        
