length = float(input("Enter length in inches (negative value to quit): "))
cm= length * 2.54

while(length>=0):
    print(f"{length} inches is {cm:0.2f} centimeters")
    length = float(input("Enter length in inches (negative value to quit): "))
    cm= length * 2.54
    
    
while(length<0):
    print("Program ended.")
    break