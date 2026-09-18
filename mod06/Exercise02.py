num = []
while True:
    num_inp = input("Enter a number: ")
    if num_inp == "":
        break
    else:
        num.append(float(num_inp))

num.sort(reverse=True)

print("The greatest numbers in descending order: ")

for n in num[:5]:
    print(f"{n:0.1f}")