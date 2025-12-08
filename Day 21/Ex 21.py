# Fibonacci with Function
def fibonacci(n):
    a = 0
    b = 1
    i = 0
    while i < n:
        print(a, end=" ")
        a, b = b, a + b
        i += 1


fibonacci(5)
# Fibonacci with return
def fibonacci(n):
    a = 0
    b = 1
    i = 0
    fib_list = []
    while i < n:
        fib_list.append(a)
        a, b = b, a + b
        i += 1
    return fib_list

print(fibonacci(7))

