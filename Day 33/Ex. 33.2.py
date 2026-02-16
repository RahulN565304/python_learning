class Library:
    
    total_books = 0

    def __init__(self, book):
        self.book = book
        Library.total_books += 1

b1 = Library("Harry Potter")
b2 = Library("Game of Thrones")
b3 = Library("Stranger Things")
b4 = Library("Interseller")
b5 = Library("Interception")

print(b1.book)
print(b2.book)
print(b3.book)

print("Total Books are: ", Library.total_books)