
s=0
matrix=[[0,1,1,2],[0,5,0,0],[2,0,3,3]]
for i in range(0,len(matrix)-1):
    for j in range(len(matrix[i])):
        if matrix[i][j]==0:
            matrix[i+1][j]=0

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
                   s=s+matrix[i][j]
                   
print(m)
print(s)
