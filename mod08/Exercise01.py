month_season={
    12:"winter",
    1:"winter",
    2:"winter",
    3:"spring",
    4:"spring",
    5:"spring",
    6:"summer",
    7:"summer" ,
    8:"summer",
    9:"autumn",
    10:"autumn",
    11:"autumn"
}

month_inp = int(input("Enter the number of a month (1-12): "))

def get_season(month_number):
    return month_season[month_number]

if month_inp in range(1,13):
    season = get_season(month_inp)
    print(f"You entered: {month_inp}")
    print(f"The season is {season}.")
else:
    print(f"You entered: {month_inp}")
    print("Please enter a number between 1 and 12.")
