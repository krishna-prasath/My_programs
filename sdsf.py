a=int(input("enter"))
s=0
for i in range(2,11):
   if a%i==0:
       s=s+1
if s==1:
    print("prime")
else:
    print("not a prime")
