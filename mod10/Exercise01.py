class Elevator:
    def __init__(self,bottom_floor,top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.floor = bottom_floor
        
    def floor_up(self):
        self.floor += 1
        
    def floor_down(self):
        self.floor -= 1
        
    def go_to_floor(self, floor_number):
        
        if floor_number > self.floor:
            while floor_number != self.floor:
                self.floor_up()
                
        elif floor_number < self.floor:
            while floor_number != self.floor:
                self.floor_down()