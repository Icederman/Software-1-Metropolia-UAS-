import random
user_randpoints = int(input("Enter number of random points to generate: ")) 

generation = 0
N_rand = 0
n_circlepoints= 0

while generation != user_randpoints:
    x = random.uniform(-1,1)
    y = random.uniform(-1,1)
    generation += 1
    N_rand += 1
    if (x**2+y**2) < 1:
        n_circlepoints += 1
        
pie_value = float((4 * n_circlepoints) / N_rand)
print(f"Approximation of pi: {pie_value:{0.4}}")