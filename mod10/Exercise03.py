class Elevator:
    def __init__(self,bottom_floor,top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = bottom_floor
        
    def floor_up(self):
        self.current_floor += 1
        
    def floor_down(self):
        self.current_floor -= 1
        
    def go_to_floor(self, floor_number):
        
        if floor_number > self.current_floor:
            while floor_number != self.current_floor:
                self.floor_up()
                
        elif floor_number < self.current_floor:
            while floor_number != self.current_floor:
                self.floor_down()

class Building:
    def __init__(self,bottom_floor,top_floor,elevators):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.elevator = elevator
        
        for i in range(self.elevator):
            elevators = []
            elevator_i = Elevator(self.bottom_floor,self.top_floor)
            elevators.append(elevator_i)
        
    def run_elevator(self,number_of_elevators,floor_number):
        pass
    
    def fire_alarm(self):
        for e in elevators:
            e.current_floor = bottom_floor