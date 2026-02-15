class movie:
    def __init__(self, name, type, year, for_kids):
        self.name = name
        self.type = type
        self.year = year
        self.for_kids = for_kids

    def enjoy(self):
        print(f"You enjoy the {self.name}")

    def dislike(self):
        print(f"You dislike the {self.name}")   

    def describe(self):
        print(f"{self.year} {self.name} {self.type}")         

movie1 = movie("Interseller", "Adventure", 2013, True)
movie2 = movie("Manmadhan", "Romance", 2015, False)
movie3 = movie("Anabelle", "Horror", 2014, False)

print(movie1.name)
print(movie2.type)
print(movie3.for_kids)
movie1.enjoy()
movie2.dislike()
movie3.describe()
