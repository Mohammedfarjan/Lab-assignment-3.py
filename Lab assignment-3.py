Here's a sample implementation of the Book Class Design, Inventory Manager, File Persistence with JSON, Menu-Driven Command Line Interface, Exception Handling and Logging, and Packaging the Project:

book.py
import json

class Book:
    def _init_(self, title, author, isbn, status="available"):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.status = status

    def _str_(self):
        return f"{self.title} by {self.author}, ISBN: {self.isbn}, Status: {self.status}"

    def to_dict(self):
        return {
            "title": self.title,
            "author": self.author,
            "isbn": self.isbn,
            "status": self.status
        }

    def issue(self):
        if self.status == "available":
            self.status = "issued"
            return True
        return False

    def return_book(self):
        if self.status == "issued":
            self.status = "available"
            return True
        return False

    def is_available(self):
        return self.status == "available"
inventory.py
import json
from pathlib import Path
from book import Book

class LibraryInventory:
    def _init_(self, file_path):
        self.file_path = Path(file_path)
        self.books = self.load_books()

    def load_books(self):
        try:
            if self.file_path.exists():
                with open(self.file_path, "r") as file:
                    data = json.load(file)
                    return [Book(**book) for book in data]
            return []
        except json.JSONDecodeError:
            print("Error: Unable to load books from file.")
            return []

    def save_books(self):
        try:
            with open(self.file_path, "w") as file:
                json.dump([book.to_dict() for book in self.books], file, indent=4)
        except Exception as e:
            print(f"Error: Unable to save books to file. {e}")

    def add_book(self, book):
        self.books.append(book)
        self.save_books()

    def search_by_title(self, title):
        return [book for book in self.books if book.title.lower() == title.lower()]

    def search_by_isbn(self, isbn):
        return [book for book in self.books if book.isbn == isbn]

    def display_all(self):
        for book in self.books:
            print(book)

    def issue_book(self, isbn):
        book = next((book for book in self.books if book.isbn == isbn), None)
        if book and book.issue():
            self.save_books()
            return True
        return False

    def return_book(self, isbn):
        book = next((book for book in self.books if book.isbn == isbn), None)
        if book and book.return_book():
            self.save_books()
            return True
        return False
main.py
import logging
from inventory import LibraryInventory

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    inventory = LibraryInventory("books.json")

    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. Issue Book")
        print("3. Return Book")
        print("4. View All Books")
        print("5. Search Book")
        print("6. Exit")

        choice = input("Enter your choice: ")

        try:
            if choice == "1":
                title = input("Enter book title: ")
                author = input("Enter book author: ")
                isbn = input("Enter book ISBN: ")
                book = Book(title, author, isbn)
                inventory.add_book(book)
                logging.info(f"Book '{title}' added successfully.")
            elif choice == "2":
                isbn = input("Enter book ISBN: ")
                if inventory.issue_book(isbn):
                    logging.info(f"Book with ISBN '{isbn}' issued successfully.")
                else:
                    logging.error(f"Book with ISBN '{isbn}' is not available.")
            elif choice == "3":
                isbn = input("Enter book ISBN: ")
                if inventory.return_book(isbn):
                    logging.info(f"Book with ISBN '{isbn}' returned successfully.")
                else:
                    logging.error(f"Book with ISBN '{isbn}' is not issued.")
            elif choice == "4":
                inventory.display_all()
            elif choice == "5":
                title = input("Enter book title: ")
                books = inventory.search_by_title(title)
                if books:
                    for book in books:
                        print(book)
                else:
                    print("Book not found.")
            elif choice == "6":
                break
            else:
                print("Invalid choice. Please try again.")
        except Exception as e:
            logging.error(f"An error occurred: {e}")

if _name_ == "_main_":
    main()
README.md
# Library Management System

A simple library management system implemented in Python.

## Features
* Add, issue, and return books
* Search books by title or ISBN
* View all books
* Save and load book data from a JSON file

## Requirements
* Python 3.8+
* json and pathlib libraries (included with Python)

## Usage
1. Run python main.py to start the application.
2. Follow the menu prompts to interact with the system.

.gitignore
*.json
_pycache_/

requirements.txt
# No dependencies required

This implementation includes the Book class, LibraryInventory class, file persistence with JSON, menu-driven command line interface, exception handling, and logging. The project is also packaged with a README file, .gitignore file, and requirements.txt file.