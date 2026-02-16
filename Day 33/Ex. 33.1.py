class Employee:

    employee_count = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.employee_count += 1

emp1 = Employee("Rahul", 60000)
emp2 = Employee("Akash", 70000)
emp3 = Employee("Uppal", 80000)

print(emp1.name, emp1.salary)
print(emp2.name, emp2.salary)
print(emp3.name, emp3.salary)

print("Total Employees:", Employee.employee_count)
