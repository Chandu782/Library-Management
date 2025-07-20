class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def __str__(self):
        status = "Borrowed" if self.is_borrowed else "Available"
        return f"{self.title} by {self.author} - [{status}]"

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author):
        new_book = Book(title, author)
        self.books.append(new_book)
        print(f"✅ '{title}' added to the library.")

    def display_books(self):
        if not self.books:
            print("❌ No books in the library.")
            return
        print("\n📚 Available Books:")
        for book in self.books:
            print(f"- {book}")

    def borrow_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                if book.is_borrowed:
                    print("❌ Book is already borrowed.")
                    return
                book.is_borrowed = True
                print(f"✅ You borrowed '{book.title}'.")
                return
        print("❌ Book not found.")

    def return_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                if not book.is_borrowed:
                    print("❌ This book was not borrowed.")
                    return
                book.is_borrowed = False
                print(f"✅ You returned '{book.title}'.")
                return
        print("❌ Book not found.")

# -------------------------------

def main():
    library = Library()

    while True:
        print("\n======== Library Menu ========")
        print("1. Add Book")
        print("2. Show All Books")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. Exit")
        print("===============================")

        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter Book Title: ")
            author = input("Enter Author Name: ")
            library.add_book(title, author)

        elif choice == '2':
            library.display_books()

        elif choice == '3':
            title = input("Enter Book Title to Borrow: ")
            library.borrow_book(title)

        elif choice == '4':
            title = input("Enter Book Title to Return: ")
            library.return_book(title)

        elif choice == '5':
            print("Exiting Library. Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
