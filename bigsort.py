unsorted=[1,
10,
3,
3,
31415926535897932384626433832795,
5]
c=0
for i in range(len(unsorted)):
    for j in range(i+1,len(unsorted)):
         if unsorted[i]>unsorted[j]:
                c=unsorted[i]
                unsorted[i]=unsorted[j]
                unsorted[j]=c

print(unsorted)
