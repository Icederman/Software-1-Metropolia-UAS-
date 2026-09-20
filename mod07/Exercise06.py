import math
def calculate_unit_price(diameter,price):
    r = diameter / 200
    area = r ** 2 * math.pi
    unit_price = price / area
    return unit_price
    
diameter_first = float(input("Enter the diameter of the first pizza (cm): "))
price_first = float(input("Enter the price of the first pizza (euros): "))

diameter_second = float(input("Enter the diameter of the second pizza (cm): "))
price_second = float(input("Enter the price of the second pizza (euros): "))
    
unit_first_price = calculate_unit_price(diameter_first, price_first)
unit_second_price = calculate_unit_price(diameter_second, price_second)

print(f"Unit price of the first pizza: {unit_first_price:0.2f} euros/m²")
print(f"Unit price of the second pizza: {unit_second_price:0.2f} euros/m²")

if(unit_first_price > unit_second_price):
    print("The second pizza provides better value for money.")
else:
    print("The first pizza provides better value for money.")