import random
v="Hi hell0 how arent you iam engineer/"
v=v.split()
print(v)
for i in range(len(v)):
    if len(v[i])>3 and (v[i][-1]=="," or v[i][-1]=="." or v[i][-1]=="?" or v[i][-1]=="!"):
        s=list(v[i][1:-3])
        random.shuffle(s)
        v[i]=v[i][0]+"".join(s)+v[i][-1]
        print(v[i])
    else:
        s=list(v[i][1:-1])
        random.shuffle(s)
        v[i]=v[i][0]+"".join(s)+v[i][-1]
        print(v[i])
v=" ".join(v)
print(v)

