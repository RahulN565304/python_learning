

rows = int(input("Enter thr number of rows: "))
columns = int(input("Enter the number of columns: "))
symbol = input("Enter the symbol: ")

for x in range(rows):
    for y in range(columns):
        print(symbol, end = "")
    print()

for i in range(1,11):
    for j in range(1,5):
        print(f"{i} x {j} = {i*j}")
        print()




