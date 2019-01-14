import math
n=1230
l=[]
l1=[]
n=str(n)
e=len(n)
a=e/2
b=0
for i in range(0,math.floor(a)):
    l.append(n[i])
for i in range(math.floor(a),e):
    l1.append(n[i])
print(l)
print(l1)
for i in range(0,len(l)):
    b=b+int(l[i])
print(b)
print(sum(int(l)))
