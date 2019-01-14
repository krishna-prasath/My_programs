def fibbo(a,b,c):
    c=a+b
    a=b
    b=c
    print(c)
    c=0
    return c+fibbo(a,b,c)

fibbo(0,1,0)
