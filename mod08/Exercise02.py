names = set()

while True:
    name_inp = str(input("Enter a name: "))
    
    if name_inp == "":
        break
    
    elif name_inp in names or name_inp.lower() in names:
        print("Existing name")
        names.add(name_inp)
    else:
        print("New name")
        names.add(name_inp)

for n in names:
    print(n)