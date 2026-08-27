import random

#For 3 digit code
firstDigit_three = random.randint(0,9)
secondDigit_three = random.randint(0,9)
thirdDigit_three = random.randint(0,9)

#For 4 digit code
firstDigit_four = random.randint(1,6)
secondDigit_four = random.randint(1,6)
thirdDigit_four = random.randint(1,6)
fourDigit_four = random.randint(1,6)


print(f"3-digit code: {firstDigit_three}{secondDigit_three}{thirdDigit_three}")
print(f"4-digit code: {firstDigit_four}{secondDigit_four}{thirdDigit_four}{fourDigit_four}")