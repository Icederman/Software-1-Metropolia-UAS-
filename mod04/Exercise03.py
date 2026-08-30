normal_male_hemoglobin = range(134,167)
low_male_hemoglobin = 134


normal_female_hemoglobin = range(117,155)
low_female_hemoglobin = 117




user_input = input("Enter biological gender (male/female): ")

user_gender= user_input.lower()

user_hemoglobin = float(input("Enter hemoglobin value (g/l): "))    

if user_gender == "male":
    
    if user_hemoglobin < low_male_hemoglobin:
        print("Your hemoglobin is low.")
    
    elif user_hemoglobin in normal_male_hemoglobin:
        print("Your hemoglobin is normal.")
    
    else:
        print("Your hemoglobin is high.")
        
elif user_gender == "female":
    
     if user_hemoglobin < low_female_hemoglobin:
        print("Your hemoglobin is low.")
    
     elif user_hemoglobin in normal_female_hemoglobin:
        print("Your hemoglobin is normal.")
    
     else:
        print("Your hemoglobin is high.")
        
else:
    print("Invalid gender.")