numbers = (-6,-5,-4,-3,2)

def get_max(num_list):
    max = num_list[0]
    for n in num_list:
        if n > max:
            max = n
    return max
result = get_max(numbers)
print(f"The max number is {result}")