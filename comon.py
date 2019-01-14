s1="zzzzzz"
s2="zzzzzzzz"
s=0
for i in range(max(len(s1),len(s2))):
    for j in range(len(s2)):
        if s1[i]==s2[j]:
            s=s+1;
        
    break
    
    
print(s)
