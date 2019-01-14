s=[]
s1=[]
q=0
a1=0
a=2
b=7
l=[]
sum1=0
for i in range(a,b+1):
    s.append(i)
for i in range(0,len(s)):
    s1.append(bin(s[i]))
print(s1)
c=""
z=c.join(s1)
print(z,len(z))
for i in range(0,len(z)):
    if str(z[i])=="1":
        sum1=sum1+1
    
print(sum1)
