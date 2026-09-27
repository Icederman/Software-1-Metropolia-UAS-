import random

class Car:
    def __init__(self,license_plate,maximum_speed=142,current_speed=0,travelled_distance=0):
        self.license_plate = license_plate
        self.maximum_speed = maximum_speed
        self.current_speed = current_speed
        self.travelled_distance = travelled_distance
    
    def accelerate(self,change_of_speed):
        if change_of_speed > 0 and self.current_speed + change_of_speed < self.maximum_speed:
            self.current_speed += change_of_speed
        elif self.current_speed + change_of_speed < 0:
            self.current_speed = 0    
        
    def drive(self,hours):
        distance = self.current_speed * hours
        self.travelled_distance += distance
    
car1 = Car("ABC",1)
car2 = Car("DEF",2)
car3 = Car("GHI",3)

cars = [car1,car2,car3]
        
def race(cars):
    hours = 0
    race_finished = False
        
    while race_finished == False:
        hours += 1
        cars[0].accelerate(random.uniform(-10.0,15.0))
        cars[0].drive(hours)
        cars[1].accelerate(random.uniform(-10.0,15.0))
        cars[1].drive(hours)
        cars[2].accelerate(random.uniform(-10.0,15.0))
        cars[2].drive(hours)
    
        for c in cars:
            if c.travelled_distance >= 10000:
                race_finished = True
                
    return cars