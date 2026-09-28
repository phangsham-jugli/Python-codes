#Attribute
class Student:
    pass

s1=Student()
s2=Student()

#attributes
s1.name="John"
s1.roll=202

print(s1.name)
print(s1.roll)

print(s1.__dict__)