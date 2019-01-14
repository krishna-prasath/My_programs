matrix=[[0,1,1,2],[0,5,0,0],[2,0,3,3]]




s=0
for r in range(0,len(matrix)-1):
    for c in range(0,len(matrix[r])):
        if matrix[r][c]==0 and matrix[r+1][c]!=0:
            s=s+0
            
        else:
            s=s+matrix[r][c]
print(s)
