number_list = [1, 2, 3, 4, 5]
def sum_of_list(number_list):
    num_sum = 0
    for n in number_list:
        num_sum += n
    return num_sum
    
result = sum_of_list(number_list)
print(f"The sum of the numbers in the list is: {result}")