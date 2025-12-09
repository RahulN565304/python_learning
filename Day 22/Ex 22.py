# For loop with Fns
numbers = [-5, -2, -9, -1]

def find_max(numbers):
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num

print(find_max(numbers))

numbers = [-5, -2, -9, -1, 0]
# While loop with Fns
def find_max(numbers):
    max_num = numbers[0]
    i = 0
    while i < len(numbers):
        if numbers[i] > max_num:
            max_num = numbers[i]
        i += 1
    return max_num

print(find_max(numbers))
# No I/p Numbers
def find_max(numbers):
    if not numbers:
        return None

    max_num = numbers[0]
    i = 0
    while i < len(numbers):
        if numbers[i] > max_num:
            max_num = numbers[i]
        i += 1
    return max_num

print(find_max([-3,-2,-1,0,1,2]))
print(find_max([]))
print(find_max(["apple", "tomato", "pear"]))
