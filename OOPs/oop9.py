#Inheritance
#single inheritance
class Vehicle:
    company="xyz motors"

    def __init__(self,wheels,seats,mileage):
        self.wheels=wheels
        self.seats=seats
        self.mileage=mileage

    def get_details(self):
        return f"This Vehicle has {self.wheels} wheels ,{self.seats} seats and provide a mileage of {self.mileage} "

class Car(Vehicle):
    def __init__(self,Car_name,drive_type):
        self.Car_name=Car_name
        self.drive_type=drive_type
        #calling parent init
        super().__init__(6,7,22)

    def get_Car(self):
        return f"name of car {self.Car_name} and drive type is {self.drive_type} "

#parent class -Vehicle
v1=Vehicle(4,6,10)
print(v1.get_details())
print("\n")

#child class
c1=Car("Porsche","Automatic")
c_detail=c1.get_Car()
print(c_detail)

#child class using parent variable and methods
print(c1.company)

details=c1.get_details()
print(details)
