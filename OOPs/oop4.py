#Arguments in instance method
class My_Class:
    def add(self,a,b):  # a and b are argument that receive values from user
        ad=a+b
        return ad

    def mul(self,a,b):
        m=a*b
        return m

obj1=My_Class()

result=obj1.add(3,4) #calling method using object
result2=obj1.mul(3,4)
print(f"sum of 3 and 4 is :{result}")
print(f"Multiplication of 3*4:{result2}")

