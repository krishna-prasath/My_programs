a=[1,2,4,8]
a1=[]
for i in range(1,len(a)+1):
    a1.append(format(a[-i],'08b'))
print(int("".join(a1),2))

