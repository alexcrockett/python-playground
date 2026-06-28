# This script defines the data structure for books and the librarian class.
# It allows for the storage and management of books in a library.

# BOOK class: Represents a book with a title, genres, and author.
# LIBRARIAN class: Manages the collection of books in the library, including adding and saving books.

# Import necessary libraries
import json


# Define the BOOK class
class BOOK:
    # Represents a book with a title, genres, and author.
    def __init__(self, title, genres, author):
        self.title = title
        self.genres = genres
        self.author = author

    # Converts the book to a dictionary for easy serialization
    # This is used for saving the book to a file.
    def to_dict(self):
        return {"title": self.title, "genres": self.genres, "author": self.author}

    # Returns a string representation of the book
    # This is used for displaying the book's information.
    def __str__(self):
        return f"{self.title}, genres = '{', '.join(self.genres)}', author = '{self.author}'"


# Represents a librarian who manages a collection of books.
class LIBRARIAN:
    # Initializes the librarian with a path to the book database file.
    def __init__(self, db_path="BookDatabase.json"):
        self.books = []  # List to store the books in the library
        self.db_path = db_path
        self.load_books()  # Load the books from the database file

    # Adds a new book to the library if it doesn't already exist.
    def add_book(self, title, genres, author):
        if not any(
            book.title == title and book.author == author for book in self.books
        ):
            new_book = BOOK(title, genres, author)
            self.books.append(new_book)
            self.save_books()  # Save the updated books list to file
            print(title + "  added successfully!")
        else:
            print("This book is already in your library.")

    # Saves the current books list to the database file.
    def save_books(self):
        with open(self.db_path, "w") as f:
            json.dump([book.to_dict() for book in self.books], f, indent=4)

    # Loads the books from the database file.
    def load_books(self):
        try:
            with open(self.db_path, "r") as f:
                books_data = json.load(f)
                self.books = [BOOK(**book) for book in books_data]
        except FileNotFoundError:
            self.books = []
            print(
                f"No existing book database found at {self.db_path}, starting with an empty library."
            )
        except json.JSONDecodeError:
            self.books = []
            print(
                f"Corrupted or empty JSON in {self.db_path}, starting with an empty library."
            )

    # Finds and prints books by a specific genre.
    def find_books_by_genre(self, genre):
        found_books = [book for book in self.books if genre in book.genres]
        for book in found_books:
            return [book for book in self.books if genre.lower() in book.genres]

    # Finds and prints books by a specific title.
    def find_books_by_title(self, title):
        # Find and print books by specific title
        found_books = [book for book in self.books if title in book.genres]
        for book in found_books:
            print(book)

    # Finds and prints books by a specific author.
    def find_books_by_author(self, author):
        found_books = [book for book in self.books if author in book.author]
        for book in found_books:
            print(book)
