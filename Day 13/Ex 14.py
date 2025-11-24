
#To find a Factorial of a number

num = int(input("Enter the number: "))
fact = 1

for i in range(1, num+1):
    fact *= i

print(f"The factorial of {num} is : {fact}")

#Printing Patters

rows = int(input("Enter the rows: "))

symbol = input("Enter the symbol: ")

for i in range(1, rows+1):
    for j in range(1, i+1):
        print(symbol, end = "")

    print()

#To find a Max/Min num

numbers = (4,7,2,9,1)
max_value = numbers[0]
min_value = numbers[0]

for num in numbers:
    if num > max_value:
        max_value = num
    elif num < min_value:
        min_value = num
print(f"The maximum num is: {max_value}")
print(f"The minimum num is: {min_value}")

#To find Fibonacci series

n = int(input("Enter the n term: "))
a, b = 0, 1
for i in range(n):
    print(a, end = " ")
    a, b = b, a+b

