# While Loop(rev)
num = 1234
rev = 0

while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10

print("Reversed number:", rev)
# While loop(total of digits)
num = 567
total = 0
while num > 0:
    digit = num % 10
    total = total + digit
    num = num // 10
print("Sum of a digits: ", total)
# Nested loop (Half Diamond)
rows = 4
for i in range(1, rows+1):
    for j in range(i):
        print("*" , end = " ")
    print()

rows = 4
for i in range(rows-1,0,-1):
    for j in range(i):
        print("*" , end = " ")
    print()
# Nested loop(Num diamond)
rows = 4
for i in range(1, rows+1):
    print(" " * (rows - i), end = "")
    print((str(i) +" ") * i)

for i in range(rows-1, 0, -1):
    print(" " * (rows - i), end ="")
    print((str(i) +" ") * i)




