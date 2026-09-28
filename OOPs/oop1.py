# Introduction to OOPs
# Classes and Objects
# Creating classes and objects
# Attributes
# Instance methods


# Creating a class
class Student:

    # Instance method
    def study(self):
        print("The student studies for 3 hour a day")


# Creating objects
s1 = Student()
s2 = Student()


# Adding attributes
s1.name = "John"
s1.roll = 202

s2.name = "Mark"
s2.roll = 203


# Accessing attributes
print(s1.name)
print(s1.roll)

print(s2.name)
print(s2.roll)


# Displaying attributes using __dict__
print(s1.__dict__)
print(s2.__dict__)


# Calling instance method
s1.study()
s2.study()