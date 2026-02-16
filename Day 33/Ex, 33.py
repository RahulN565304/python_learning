class student:

    school = "ABC School"

    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

student1 = student("Abishek", 300)
student2 = student("Aishwarya", 301)
student3 = student("Arun", 302)

print(student1.name)
print(student2.name)
print(student3.name)
print(student1.school)
print(student2.school)
print(student3.school)

