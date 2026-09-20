import random
sides = int(input("Enter number of sides: "))
def roll_dice(sides):
    rolled_num = random.randint(1,sides)
    return rolled_num
    
new_rolled_num = roll_dice(sides)
print(new_rolled_num)

while new_rolled_num != sides:
    new_rolled_num = roll_dice(sides)
    print(new_rolled_num)