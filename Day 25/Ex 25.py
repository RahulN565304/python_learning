# Using Slicing to Rev the List

arr = [10, 20, 30, 40, 50]

rev_arr = arr[::-1]
print("Reversed array:", rev_arr)

arr = [12, 45, 7, 23, 89, 34]

# Maximum Value using Array

max_value = arr[0]
for x in arr:
    if x > max_value:
        max_value = x
print("Maximum Value is:", max_value)

# To find Duplicates

arr = [1, 2, 3, 2, 4, 5, 1]

duplicates = []

for x in arr:
    if arr.count(x) > 1 and x not in duplicates:
        duplicates.append(x)

print("Duplicates:", duplicates)

# To find Duplicates(1)

arr = [1, 2, 3, 2, 4, 5, 1]

seen = set()
dups = set()

for x in arr:
    if x in seen:
        dups.add(x)
    else:
        seen.add(x)

print("Originals:", list(seen))
print("Duplicates:", list(dups))
