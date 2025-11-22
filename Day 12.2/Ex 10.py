numbers = (22,33,44,55,66)

def get_num(num_list):
    total = 0
    for n in num_list:
        total += n
    return total
result = get_num(numbers)
print(f"The sum of numbers is: {result}")