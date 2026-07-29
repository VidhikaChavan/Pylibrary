# Base class: Book
class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = True

    def display_info(self):
        status = "Available"
        if self.available==True:
            pass 
        else :
            return "Checked Out"
        print(f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}, Status: {status}")


# Derived class: Member
class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.available:
            book.available = False
            self.borrowed_books.append(book)
            print(f"{self.name} borrowed '{book.title}'")
        else:
            print(f"Sorry, '{book.title}' is not available.")

    def return_book(self, book):
        if book in self.borrowed_books:
            book.available = True
            self.borrowed_books.remove(book)
            print(f"{self.name} returned '{book.title}'")
        else:
            print(f"{self.name} does not have '{book.title}' borrowed.")


# Derived class: Librarian (inherits from Member)
class Librarian(Member):
    def __init__(self, name, member_id, employee_id):
        super().__init__(name, member_id)
        self.employee_id = employee_id

    def add_book(self, library, book):
        library.books.append(book)
        print(f"Librarian {self.name} added '{book.title}' to the library.")

    def remove_book(self, library, book):
        if book in library.books:
            library.books.remove(book)
            print(f"Librarian {self.name} removed '{book.title}' from the library.")
        else:
            print(f"'{book.title}' not found in the library.")


# Library class (composition, not inheritance)
class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def show_books(self):
        print(f"\nBooks in {self.name}:")
        for book in self.books:
            book.display_info()


# Example usage
if __name__ == "__main__":
    # Create library
    my_library = Library("City Library")

    # Create books
    book1 = Book("1984", "George Orwell", "12345")
    book2 = Book("To Kill a Mockingbird", "Harper Lee", "67890")

    # Create members
    member1 = Member("Alice", "M001")
    librarian = Librarian("Bob", "M002", "L001")

    # Librarian adds books
    librarian.add_book(my_library, book1)
    librarian.add_book(my_library, book2)

    # Show books
    my_library.show_books()

    # Member borrows a book
    member1.borrow_book(book1)

    # Show books again
    my_library.show_books()

    # Member returns book
    member1.return_book(book1)

    # Librarian removes a book
    librarian.remove_book(my_library, book2)

    # Final state
    my_library.show_books()
