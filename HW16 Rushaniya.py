# number 1
'''class Vehicle():
    def __init__(self,model,year):
        self.model=model
        self.year=year
class Car(Vehicle):
    def __init__(self,model,year,fuel):
        self.fuel=fuel
vehicle=Vehicle("Mitsubishi",2020)

car=Car("Mitsubishi",2020,"Diesel")
  
print(car)'''

#number 3
'''class Vehicle():
    def __init__(self,model,year):
        self.model=model
        self.year=year
class Car(Vehicle):
    def __init__(self,model,year,fuel):
        self.fuel=fuel
vehicle1=Vehicle("Mitsubishi",2020)
vehicle2=Vehicle("Tesla",2022)
vehicle3=Vehicle("Toyota",2021)
vehicle4=Vehicle("Ford",2023)

car1=Car("Mitsubishi",2020,"Diesel")
car2=Car("Tesla",2022,"Charging batteries")
car3=Car("Toyota",2021,"AI96")
car4=Car("Ford",2023,"AI92")

    
print(car4)'''

#number 2
class Animal():
    def x(self):
       return f"This is an animal"
class Flyable():
    def fly(self):
        return f"It is flyable"
class Bird (Animal, Flyable):
    def __init__(self,type):
        self.type=type
bird= Bird("sparrow")

print(bird.x)
print(bird.fly)

