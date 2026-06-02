class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        
    def move(self):
        print(f"The vehicle {self.brand} {self.model} is moving")
        
    def stop(self):
        print(f"The vehicle {self.brand} {self.model} is stopping")
        
class Car(Vehicle):
    def fuel_type(self):
        print("Petrol")
        
class Truck(Vehicle):
    def fuel_type(self):
        print("Diesel")
        
class Train(Vehicle):
    def fuel_type(self):
        print("coal")
        
    def run(self):
        print(f"The train runs on the track")
        
car = Car("Porsche", "911 GT Rs")
truck = Truck("Scania", "770S V8")
train = Train("GE", "ES44AC")

print(car.brand)
print(truck.brand)
train.run()
truck.fuel_type()