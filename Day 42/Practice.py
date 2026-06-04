class Instrument:
    def __init__(self, name):
        self.name = name

class Guitar(Instrument):
    def __init__(self, name, number_of_string):
        super().__init__(name)
        self.number_of_string = number_of_string

    def __str__(self):
        return f"{self.name} with {self.number_of_string}"
       
class Drum(Instrument):
    def __init__(self, name, drum_type):
        super().__init__(name)
        self.drum_type = drum_type

    def __str__(self):
        return f"{self.name} with {self.drum_type}"
        
class Piano(Instrument):
    def __init__(self, name, number_of_keys):
        super().__init__(name)
        self.number_of_keys = number_of_keys

    def __str__(self):
        return f"{self.name} with {self.number_of_keys}"

guitar = Guitar("Yamaha Guitar", 10)
drum = Drum("Roland Drum", "Electronic")
piano = Piano("Steinway Piano", 88)

print(piano)
print(guitar)
print(drum)

