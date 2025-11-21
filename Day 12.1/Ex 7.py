total_bill_amount = float(input("Enter the total bill amount: "))
tip_percentage = int(input("Enter the tip percentage: "))
num_people = int(input("Enter the number of people: "))

tip_amount = (tip_percentage / 100) * total_bill_amount
total_with_tip = total_bill_amount + tip_amount
per_person = total_with_tip / num_people

print(round(per_person, 2))
print(f"Each person should pay: {round(per_person, 2)}")

