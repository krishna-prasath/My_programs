a="Programmer"
c=0
z=0
x=""
for i in range(len(a)):
    if a[i]=="r":
        c=c+1
    if a[i]=="g":
        z=i-1
    if a[i]!="m":
        x=x+a[i]
    else:
        x=x+"Y"
print("occurence of "r":",c)
print("position of g:",z)
print("replaced string",x)

    
