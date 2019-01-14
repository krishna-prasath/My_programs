x=31
y=118
for i in range(0,32):
    if (i*2)+((x-i)*4)==y:
        break
print(i,x-i)
