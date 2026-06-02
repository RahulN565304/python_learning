class Car:
    def fuel_type(self):
        print("Petrol")
        
class Truck:
    def fuel_type(self):
        print("Diesel")
        
class Train:
    def fuel_type(self):
        print("Coal")
        
vehicles = [Car(), Truck(), Train()]

for vehicle in vehicles:
    vehicle.fuel_type()