#Static Method
#Class method
class Student:
    college="ABC University of Poop people"
    Dept=["Arts","Science","Commerce"]

    def __init__(self,name,roll):
        self.name=name
        self.roll=roll
    def study(self,n):
        print(f"Student studies for an {n} hour")

    @staticmethod
    def greet():
        print("Welcome to college!")

    @classmethod
    def clg_name(cls):
        print(cls.college)

    @classmethod
    def dept_name(cls):
        print("Department are:")
        for i in cls.Dept:
            print(i)





#initializer
s1=Student("Rohit",11)
print(s1.name,s1.roll)

print("\n")
#calling class method
s1.greet()
s1.clg_name()
s1.dept_name()

print("\n")
#Using object method study()
s1.study(4)

print("\n")
#using class variable
print(s1.college)
print(s1.Dept)


