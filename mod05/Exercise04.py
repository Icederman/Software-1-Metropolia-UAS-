import random
random_intg = random.randint(1,11)

guess = int(input("Guess the integer: "))

while guess != random_intg:
    if guess > random_intg:
        print("Too high")
    else:
        print("Too low")
    guess = int(input("Guess the integer: "))
    
print("Correct")