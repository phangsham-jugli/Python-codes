#MULTILEVEL Inheritance
class Vehicle:
    company="xyz motors"

    def __init__(self,wheels,seats,mileage):
        self.wheels=wheels
        self.seats=seats
        self.mileage=mileage

    def get_details(self):
        return f"This Vehicle has {self.wheels} wheels ,{self.seats} seats and provide a mileage of {self.mileage} "

class Car(Vehicle):
    def __init__(self,Car_name,drive_type,wheels,seats,mileage):
        print("init of car")
        self.Car_name=Car_name
        self.drive_type=drive_type
        #calling parent init
        super().__init__(wheels,seats,mileage) #passed argument by car __init__ and it initialized the vehicle

    def get_info(self):
        return f"name of car {self.Car_name} and drive type is {self.drive_type} "

class ElectricCar(Car):
    def __init__(self,Car_name,drive_type,wheels,seats,mileage,battery_capacity,range):
        print("init of Electric car")
        self.battery=battery_capacity
        self.range=range
        super().__init__(Car_name,drive_type,wheels,seats,mileage) #variable pass by ev and it initialized the car

    def get_ev(self):
        print(f"this Ev has {self.battery} and give range of {self.range}")

