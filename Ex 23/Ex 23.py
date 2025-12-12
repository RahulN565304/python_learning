#Dictionary Programs
#Program 1

students = {
    "Rahul": {"math": 80, "science": 90},
    "Priya": {"math": 85, "science": 95}
    }

print(students.get("Priya").get("science"))

#Program 2

grocery = {"milk": 40, "bread": 30, "eggs": 60}

grocery.update({"rice": 100})
sum = sum(grocery.values())
print(sum)

#Program 3

scores = {"math": 85, "science": 90, "english": 78}

for score in scores.items():
   print(score)

max_value = -1
for value in scores.values():
    if value > max_value:
        max_value = value
print(max_value)
