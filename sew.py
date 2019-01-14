a=[1,3,2,1]
a1=0;
for i in range(len(a)):
    for j in range(len(a)):
        if a[i]-a[j]==0:
            a1=a1+1
        else:
            a1+=0
if a1==-1:
    print("false")
else:
    print("true")
            
