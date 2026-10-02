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
    
    
class Race:
    def __init__(self,name,distance,cars):
        self.name = name
        self.distance = distance
        self.cars = cars
        
    
    def hour_passes(self):
        for c in self.cars:
            h = 1
            c.accelerate(random.uniform(-10.0,15.0))
            c.drive(h)
            h += 1
        
    
    def print_status(self):
        for c in self.cars:
            print(f"{c.license_plate} {c.maximum_speed} {c.current_speed} {c.travelled_distance}")
           
    
    def race_finished(self):
        for c in self.cars:
                if c.travelled_distance >= self.distance:
                    race_finished = True
                    return True
                    
                else:
                    return False
                    
    
            