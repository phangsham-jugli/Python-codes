#Polymorphism -method overriding
#EG1:
class Employee:
    def working_hours(self):
        return 45

class Intern(Employee):
    def working_hours(self):
        return 30

i=Intern()
print(i.working_hours())

print("\n")

#Eg2:
class Employee:
    def working_hours(self):
        return 45

class Intern(Employee):
    pass

i=Intern()
print(i.working_hours())


