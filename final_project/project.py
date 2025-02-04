class Personal_Library:
    def __init__(self):
        self.books = []
        self.check_out_books = []

    def add_book(self, title, author):
        self.books.append({"title": title, "author": author, "status": "available"})
        print(f"Book '{title}' by {author} added to the library.")

    def remove_book(self, title):
        for book in self.books:
            if book["title"].lower() == title.lower():
                self.books.remove(book)
                print(f"Book '{title}' removed from the library.")
                return True
        print(f"Book '{title}' not found.")
        return False

    def list_books(self):
        if not self.books:
            print("No books available in the library")
        else:
            print("\nBooks in library:")
            for idx, book in enumerate(self.books, start=1):
                print(f"{idx}. {book['title']} by {book['author']} (Status: {book['status']})")

    def search_book(self, title):
        for book in self.books:
            if book["title"].lower() == title.lower():
                print(f"Found: {book['title']} by {book['author']} (Status: {book['status']})")
                return
        print(f"Book '{title}' not found in the library.")

    def update_book(self, old_title, new_title, new_author):
        for book in self.books:
            if book["title"].lower() == old_title.lower():
                book["title"] = new_title
                book["author"] = new_author
                print(f"Book '{old_title}' updated to '{new_title}' by {new_author}.")
                return True
        print(f"Book '{old_title}' not found.")
        return False

    def check_out_book(self, title):
        for book in self.books:
            if book["title"].lower() == title.lower() and book["status"] == "available":
                book["status"] = "Checked out"
                self.checked_out_books.remove(book)
                print(f"Book '{title}' returned to the library.")
                return True
        print(f"Book '{title}' was not checked out.")
        return False

def main():
    personal_library = Personal_Library()

    while True:
        print("\nLibrary Management System")
        print("1. Add a Book")
        print("2. Remove a Book")
        print("3. List all Books")
        print("4. Search for a Book")
        print("5. Update Book Details")
        print("6. Check Out a Book")
        print("7. Return a Book")
        print("8. Exit")

        choice = input("Enter your choice (1-8): ")

        if choice == "1":
            title = input("Enter the title of the book: ")
            author = input("Enter the author of the book: ")
            personal_library.add_book(title, author)
        elif choice == "2":
            title = input("Enter the title of the book to remove: ")
            personal_library.remove_book(title)
        elif choice == "3":
            personal_library.list_books()
        elif choice == "4":
            title = input("Enter the title of the book to search: ")
            personal_library.search_book(title)
        elif choice == "5":
            old_title = input("Enter the old title of the book: ")
            new_title = input("Enter the new title of the book: ")
            new_author = input("Enter the new author of the book: ")
            personal_library.update_book(old_title, new_title, new_author)
        elif choice == "6":
            title = input("Enter the title of the book to check out: ")
            personal_library.check_out_book(title)
        elif choice == "7":
            title = input("Enter the title of the book to return: ")
            personal_library.return_book(title)
        elif choice == "8":
            print("Exiting Library Management System.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
