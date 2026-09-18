num = int(input("Enter an integer: "))
is_prime = False

if num <= 1:
    is_prime = False
    
elif num == 2:
    is_prime = True
    
elif num > 3:
    for i in range(2,num):
        if num % i == 0:
            is_prime = False
            break
        else:
            is_prime = True
        
if is_prime == True:
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")