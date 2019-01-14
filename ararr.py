a=[23,85,0]
s=[]
for i in range(0,len(a)):
   
    c=bin(a[i]).lstrip("0b")
    s.append(c) 
    d=''
    
s=d.join(s)
print(int(s,2))
