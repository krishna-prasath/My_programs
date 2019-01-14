m=[[0]]
s=0
for i in range(len(m)):
    for j in range(len(m[i])):
        if m[i][j]==0 and m[i+1][j]!=0:
           s=s+0
        elif m[i][j]!=0:
            s=s+m[i][j]
        
print(s)
