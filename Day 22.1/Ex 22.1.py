# Stop in (-ve) num
def sum_until_negative():
    total = 0
    while True:
        numbers = int(input("Enter a number: "))
        if numbers < 0:
            break
        total += numbers
    return total

print(sum_until_negative())
# Squares with loop
def squares(n):
    product = 0
    sqr_list = []
    for i in range(1, n+1):
        sqr_list.append(i**2)
    return sqr_list

print(squares(7))
# Even numbers upto N
def even_numbers(n):
    even_num = []
    for i in range(1, n+1):
        if i % 2 == 0:
            even_num.append(i)
    return even_num

print(even_numbers(10))



