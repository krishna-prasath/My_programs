m=[[1, 1, 1], 
   [2,2,2], 
   [3, 3, 3]]
s=0
for i in range(len(m)-1):
    for j in range(len(m[i])):
        for j1 in range(1,len(m)):
            if m[i][j]!=0 and m[j1][j]==0:
                s=s+m[i][j]
            else:
                s=s+0
                                 
print(s)
