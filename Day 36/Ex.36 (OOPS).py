class Student:
    def __init__(self, name, roll, marks):
        self.name = name
        self.roll = roll
        self.marks = marks
        
    def grade(self):
        if self.marks >= 90:
           print("Grade A+")
        elif self.marks >= 85:
          print("Grade A")
        elif self.marks >= 65:
           print("Grade B")
        elif self.marks >= 50: 
          print("Grade C")
        elif self.marks >= 35:
            print("Grade D")
        else:
           print("Grade E")
           
    def check_result(self):
        if self.marks >= 35:
            print(f"You passed the test")
        else:
            print(f"You failed the test")
            
    def display(self):
        print(f"Name is {self.name} of roll no. {self.roll} and marks {self.marks}")
        self.grade()
        
student1 = Student("Rahul", 370, 34)
student2 = Student("Akash", 477, 70)
student3 = Student("Adhi", 315, 45)
student4 = Student("Shijey", 450, 37)

print(student1.marks)
print(student4.marks)
student2.grade()
student3.grade()
student1.check_result()
student4.check_result()
student2.display()
student3.display()


