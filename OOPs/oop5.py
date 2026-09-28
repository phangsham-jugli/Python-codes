#initializer
class student:
    def __init__(self,n,r):
        self.name=n
        self.roll=r
        self.Dept = "Science"

S1=student("John",16)
S2=student("Carol",18)

print(S1.name,S1.roll,S1.Dept)
print(S2.name,S2.roll,S2.Dept)

print(S1.__dict__)
print(S2.__dict__)