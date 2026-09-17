inputs = []

while True:
    user_inp = (input("Enter a number (or press Enter to quit): "))
    if user_inp == "":
        break
    else:
        inputs.append(float(user_inp))
    
    
small_num = min(inputs)
large_num = max(inputs)
print(f"Smallest number: {small_num:0.1f}")
print(f"Largest number: {large_num:0.1f}")