class scl:
    def __init__(self,name,rollno,marks):
        self.n=name
        self.r=rollno
        self.m=marks
    def print(self):
        return self.n,self.r,self.m

a=scl("krishna",123,87)
b=scl("prasath",124,90)
print(a.print())
print(b.print())
