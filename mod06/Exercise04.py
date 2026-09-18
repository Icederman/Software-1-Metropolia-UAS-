city_names = []

for i in range(5):
    user_inp = str(input("Enter the name of a city: "))
    city_names.append(user_inp)

print("\n\nThe cities you entered: ")
for name in city_names:
    print(name)
    