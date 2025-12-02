#While Loop1

i = 0
a = 'geeksforgeeks'

while i < len(a):
    if a[i] == 'e' or a[i] == 's':
        i += 1
        continue

    print(a[i])
    i += 1

#While Loop2
i=0
while i < 4:
    i += 1
    print(i)
    break
else:
    print("No Break")