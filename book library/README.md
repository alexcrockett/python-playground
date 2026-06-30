# Basic library manager - notes
The scripts in this directory provide a very basic home library manager that can be used to manage a collection of books. Books are stored in a JSON file. 

Available functionality includes:
- Adding books to the library
- Finding books by genre, title, or author
- Removing books from the library

## Features

- **Book Management**: Add new books to the library with details including title, genres, and author.
- **Persistent Storage**: Books are saved to a JSON file for persistence between program runs.
- **Search Functionality**: Find books by genre, title, or author.
- **Duplicate Prevention**: The system prevents adding duplicate books to the library.

## Program structure
The program consists of two main scripts:
- `LibraryClasses.py` 
- `LibraryFunctions.py`

In this architecture: 

`LibraryClasses` acts defines the classes and functions of the library, i.e. saviving and searching for books. The script also defines the data structure of a book, and provides other background definintions.

`LibraryFunctions` provides the main functionality of the user-facing application, i.e. doing the adding, finding, and removing books. It uses the classes defined in `LibraryClasses` to interact with the library data to complete these various operations.

## Components

### LIBRARIAN Class

The `LIBRARIAN` class manages the collection of books in the library. It provides functionality for:

- Adding new books to the library
- Saving the book collection to a JSON file
- Loading the book collection from a JSON file
- Searching for books by genre, title, or author

### BOOK Class

The `BOOK` class represents individual books in the library. Each book has:

- A title
- A list of genres
- An author

The class includes methods for:

- Converting book data to a dictionary format for storage
- Providing a string representation of the book

## Usage
To use the library manager, run `LibraryFunctions.py`.

1. Create a `LIBRARIAN` object to manage your library:

```python
librarian = LIBRARIAN()
```

2. Add books to your library:

```python
librarian.add_book("The Great Gatsby", ["Classic", "Fiction"], "F. Scott Fitzgerald")
```

3. Search for books:

```python
# Search by genre
librarian.find_books_by_genre("Fiction")

# Search by title
librarian.find_books_by_title("The Great Gatsby")

# Search by author
librarian.find_books_by_author("F. Scott Fitzgerald")
```

## Requirements

- Python 3.x

## Installation

1. Clone this repository to your local machine.
2. Ensure you have Python 3.x installed.
3. Run the `LibraryClasses.py` script to start managing your book library.
