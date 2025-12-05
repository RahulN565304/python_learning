# Function (Even or Odd)
def EvenorOdd(n):
    if n % 2 == 0:
        return f"{n} is an even"
    else:
        return f"{n} is an odd"


result = EvenorOdd(90)
print(f"The given num is: {result}")

# Factorial (For loop)

def factorial(n):
    result = 1
    for i in range(1, n+1):
        result = result * i
    return result

result = factorial(8)
print(f"The factorial of the num is: {result}")

# Factorial (while loop)

def factorial(n):
    result = 1
    i = 1
    while i <= n :
        result = result * i
        i+=1
    return result

result = factorial(5)
print(f"{result}")

