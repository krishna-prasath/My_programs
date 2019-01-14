new={0:'A',1:'B',2:'C',3:'D',4:'E',5:'F',6:'G',7:'H',8:'I',9:'J',10:'K',11:'L',12:'M',13:'N',14:'O',15:'P'}
print(new)
a1=[]
a2=[]

a=int(input("enter "))
for i in range(0,(a//2)+1):
    for j in range(0,a+1):
          if i+j==a:
              a1.append(i)
              a1.append(j)
print(a1)

for i in range(len(a1)-1):
    a2.append(str(a1[i])+str(a1[i+1]))
    i+=1
print(a2)

for i in range(len(a2)):
    s=list(a2[i])
    s.insert(i+1,'+')
    
    print(s)


