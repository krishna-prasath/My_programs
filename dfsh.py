a=[1,32,5,64,3,5]
a.sort(reverse=True)
print(a)
v=30

for i in range(len(a)):
    if v>a[i]:
        print(a[i])
        break
