class Student:
    college="ABC University of Poop people"
    Dept=["Arts","Science","Commerce"]

    def __init__(self,name,roll):
        self.name=name
        self.roll=roll
    def study(self,n):
        print(f"Student studies for an {n} hour")

s1=Student("Rohit",11)
print(s1.name,s1.roll)
s1.study(4)

#using class variable
print(s1.college)
print(s1.Dept)

