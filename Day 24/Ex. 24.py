
class Car:
    def __init__(self, brand, year, color, for_sale):
        self.brand = brand
        self.year = year
        self.color = color
        self.for_sale = for_sale

    def drive(self):
        print(f"You drive the {self.brand}")

    def stop(self):
        print(f"You stop the {self.brand}")

car1 = Car("Dodge", 2005, "Black", False)
car2 = Car("Tesla", 2024, "White", True)
car3 = Car("BMW", 2008, "Silver", False)

print(car3.brand)
print(car3.year)
print(car3.color)
print(car3.for_sale)
car1.drive()
car2.stop()