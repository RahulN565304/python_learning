def grocery_bill(item1, item2, item3):
    total = item1 + item2 + item3
    average = total/3
    highest = max(item1, item2, item3)
    return total, average, highest
t, a, h = grocery_bill(45, 65, 95)
print("total: ", t)
print("Average: ", a)
print("highest: ", h)
