ride_time=30
ride_distance=7
cost_per_minute=[0.2,0.35,0.4,0.45]
cost_per_mile=[1.1,1.8,2.3,3.5]
a=[]
b=[]
c=[]
for i in range(len(cost_per_minute)):
    a.append(ride_time*cost_per_minute[i])
for i in range(len(cost_per_mile)):
    b.append(ride_distance*cost_per_mile[i])

for i in range(len(cost_per_minute)):
    c.append(round(a[i]+b[i],2))

print(a)
print(b)
print(c)
