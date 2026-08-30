user_cabin_class = input("Enter the cabin class (LUX, A, B, or C): ")

if user_cabin_class == "LUX":
    print("Upper-deck cabin with a balcony.")

elif user_cabin_class == "A":
    print("Above the car deck, equipped with a window.")
    
elif user_cabin_class == "B":
    print("Windowless cabin above the car deck.")
    
elif user_cabin_class == "C":
    print("Windowless cabin below the car deck.")

else:
    print("Invalid cabin class.")