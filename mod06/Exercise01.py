import random
num_roll = int(input("How many dice to roll: "))
sum = 0
for n in range(num_roll):
        num = random.randint(1,7)
        sum += num
        
print(f"Sum of the dice: {sum}")      