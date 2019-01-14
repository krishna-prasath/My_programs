a="a(bc)de"
a=list(a)
a1=[]
for i in range(len(a)):
    if (a[i]=='(') or (a[i]==')'):
        a[i]=0

for i in range(len(a)):
    if a[i]!=0:
        a1.append(a[i])

print(a1)

print(str("".join(a1)))  
