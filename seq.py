sequence=[10,1,2,3,4,5]
sumw=0
for i in range(0,len(sequence)-2):
    for j in range(i+1,len(sequence)-1):
        if sequence[i]==sequence[j]:
            sumw=sumw+1

print(sumw)
