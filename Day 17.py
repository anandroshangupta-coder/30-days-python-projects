# ==========================================
# Day 17 - Library Management System
# 30 Days Python GitHub Project Challenge
# ==========================================


print("======================================")
print("       LIBRARY MANAGEMENT SYSTEM")
print("======================================")


# ==========================================
# Book Class
# ==========================================

class Book:

    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.available = True

    def display(self):
        status = "Available" if self.available else "Issued"

        print(f"\nBook ID : {self.book_id}")
        print(f"Title   : {self.title}")
        print(f"Author  : {self.author}")
        print(f"Status  : {status}")


# ==========================================
# Library Class
# ==========================================

class Library:

    def __init__(self):
        self.books = {}

    # Add book
    def add_book(self):

        book_id = input("\nEnter book ID: ")

        if book_id in self.books:
            print("❌ Book ID already exists.")
            return

        title = input("Enter book title: ")
        author = input("Enter author name: ")

        book = Book(book_id, title, author)

        self.books[book_id] = book

        print("✅ Book added successfully!")

    # View all books
    def view_books(self):

        print("\n======================================")
        print("             ALL BOOKS")
        print("======================================")

        if not self.books:
            print("No books available.")
            return

        for book in self.books.values():
            book.display()

        print("\n======================================")

    # Search book
    def search_book(self):

        book_id = input("\nEnter book ID to search: ")

        if book_id in self.books:
            print("\n✅ Book found!")
            self.books[book_id].display()
        else:
            print("❌ Book not found.")

    # Issue book
    def issue_book(self):

        book_id = input("\nEnter book ID to issue: ")

        if book_id not in self.books:
            print("❌ Book not found.")
            return

        book = self.books[book_id]

        if book.available:
            book.available = False
            print(f"✅ '{book.title}' has been issued.")
        else:
            print("❌ This book is already issued.")

    # Return book
    def return_book(self):

        book_id = input("\nEnter book ID to return: ")

        if book_id not in self.books:
            print("❌ Book not found.")
            return

        book = self.books[book_id]

        if not book.available:
            book.available = True
            print(f"✅ '{book.title}' has been returned.")
        else:
            print("❌ This book is already available.")

    # Delete book
    def delete_book(self):

        book_id = input("\nEnter book ID to delete: ")

        if book_id in self.books:
            deleted_book = self.books.pop(book_id)
            print(f"✅ '{deleted_book.title}' deleted successfully.")
        else:
            print("❌ Book not found.")


# ==========================================
# Create Library
# ==========================================

library = Library()


# ==========================================
# Main Menu
# ==========================================

while True:

    print("\n======================================")
    print("             LIBRARY MENU")
    print("======================================")
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Issue Book")
    print("5. Return Book")
    print("6. Delete Book")
    print("7. Exit")
    print("======================================")

    choice = input("Enter your choice (1-7): ")

    if choice == "1":

        library.add_book()

    elif choice == "2":

        library.view_books()

    elif choice == "3":

        library.search_book()

    elif choice == "4":

        library.issue_book()

    elif choice == "5":

        library.return_book()

    elif choice == "6":

        library.delete_book()

    elif choice == "7":

        print("\n======================================")
        print("   Thank You! Goodbye 👋")
        print("======================================")
        break

    else:

        print("❌ Invalid choice! Please select 1-7.")