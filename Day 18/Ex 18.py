# Compact Pattern

rows = 7
for i in range(1, rows+1):
    print(" " * (rows - i), end = " ")
    print("*" * (2*i - 1))

# Control (for loop)

for row in range(1, rows+1):
for i in range(1, 21):
    if i % 3 == 0:
        continue
    if i == 15:
        break
    print(i)

# Control (while loop)

for row in range(1, rows+1):
i = 1
while i <= 21:
    if i % 3 == 0:
        i+=1
        continue
    if i == 15:
        break
    print(i)
    i+=1


