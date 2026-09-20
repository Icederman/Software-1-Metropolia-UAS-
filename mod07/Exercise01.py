import random
def roll_dice():
    rolled_num = random.randint(1,6)
    return rolled_num
    
num = roll_dice()
print(num) 

while(num != 6):
    num = roll_dice()
    print(num)    