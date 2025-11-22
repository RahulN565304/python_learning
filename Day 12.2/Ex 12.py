numbers = (-3,-2,-1,0,1,2,3)

def get_min_max(num_list):
    max_value = 0
    min_value = 0

    for n in num_list:
        if n > max_value:
            max_value = n
        if n < min_value:
            min_value = n
    return max_value, min_value

result = get_min_max(numbers)
print(f"The max value is {result[0]}")
print(f"The min value is {result[1]}")