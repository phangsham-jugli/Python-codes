#POLYMORPHISM -method overloading
class A:
    def add(self, num1=0, num2=0, num3=0):
        return num1 + num2 + num3

obj=A()
print(obj.add(1,2))

print(obj.add(1,2,3))