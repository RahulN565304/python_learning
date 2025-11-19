operator = input("Enter an operator (+ - * / ** % //): ")
num1 = float(input("Enter the num1: "))
num2 = float(input("Enter the num2: "))

if operator == "+":
    result = num1 + num2
    print(round(result, 2))
elif operator == "-":
    result = num1 - num2
    print(round(result, 2))
elif operator == "*":
    result = num1 * num2
    print(round(result, 2))
elif operator == "/":
    result = num1 / num2
    print(round(result, 2))
elif operator == "**":
    result = num1 ** num2
    print(round(result, 2))
elif operator == "%":
    result = num1 % num2
    print(round(result, 2))
elif operator == "//":
    result = num1 // num2
    print(round(result, 2))
else:
    print("Invalid operator")