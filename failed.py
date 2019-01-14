a="ProFiLe"
b=1
c=2
a1=list(a)
if b==1:
    for i in range(0,len(a),2):
        if  (i+1)%2==0:
           a1[i]= a1[i].lower()
    print("".join(a1))
else:
    for i in range(0,len(a)):
        if  (i+1)%2==0:
           a1[i]= a1[i].upper()
    print("".join(a1))
