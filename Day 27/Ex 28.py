# Stack Reverse a str

stack = []
stack.append("h")
stack.append("e")
stack.append("l")
stack.append("l")
stack.append("o")
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack)

# Balanced Parantheses

def is_balaced(expr):
    stack = []
    pairs = {')':'(', ']' : '[', '}' : '{' }
    for ch in expr:
        if ch in "([{":
            stack.append(ch)
        elif ch in "}])":
            if not stack:
                return False
            if stack[-1] != pairs[ch]:
                return False
            stack.pop()
    return len(stack) == 0

print(is_balanced("([{}])"))
print(is_balanced("([{]})"))


