airports= {}

while True:
    print("\nAirport Data Management\n1. Enter a new airport\n2. Fetch airport information\n3. Quit")
    option_choice = int(input("Please choose an option (1-3): "))
    
    if option_choice == 1:
        code_inp = str(input("Enter the ICAO code: "))
        name_inp = str(input("Enter the airport name: "))
        airports[code_inp] = name_inp
        print(f"Airport {name_inp} with ICAO code {code_inp} has been added.")
        
    elif option_choice == 2:
        code_inp = str(input("Enter the ICAO code: "))
        if code_inp in airports.keys():
            print(f"The airport with ICAO code {code_inp} is {airports[code_inp]}.")
        else:
            print("No airport found with ICAO code EFHK.")
    elif option_choice == 3:
        print("Thank you for using the Airport Data Management system. Goodbye!")
        break