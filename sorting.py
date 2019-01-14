a=[4,7,9,12,89]
b=[2,45,67,100]
A=[]
A=a+b
a1=A
print(a1)
print(A)
# above is done using inbuilt function

# bellow is the sorting method

for i in range(len(a1)):
    for j in  range(i,len(a1)):
           if a1[i]>a1[j]:
            s=a1[i]
            a1[i]=a1[j]
            a1[j]=s
print(a1)
