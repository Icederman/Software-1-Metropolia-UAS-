am_gall = float(input("Enter a volume in American gallons (negative value to quit): "))

def gallons_to_liters(am_gall):
    conv_value = 3.785 * am_gall
    return conv_value
    

while(am_gall >= 0):
    liter_value = gallons_to_liters(am_gall)
    print(f"{am_gall:0.1f} American gallons is {liter_value:0.2f} liters.")
    am_gall = float(input("Enter a volume in American gallons (negative value to quit): "))

        
print("Program finished.")    