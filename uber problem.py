u=["UberX","UberXl","UberPlus","UberBlack","UberSuv"]
m=[0.3,0.5,0.7,1,1.3]
#m=[1,2,3,4,5]
l=20
c=20
a=[]
b=[]
for i in range(len(m)):
    a.append(m[i]*l)

for i in range(len(a)):
    if c>=a[i]:
        b.append(i)
        
print(a)
print(b)
print(u[max(b)])

