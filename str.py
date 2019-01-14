s1="absdmn"
s2="abdkffidmn"
print(len(s1))
s=0
for i in range(len(s1)):
    for j in range(len(s2)):
        if s1[i]==s2[j]:
            s=s+1
print(s)
