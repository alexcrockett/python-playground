# Basic library manager - notes
The scripts in this directory provide a very basic home library manager that can be used to manage a collection of books. Books are stored in a JSON file. 

Available functionality includes:
- Adding books to the library
- Finding books by genre, title, or author
- Removing books from the library

## Program structure
The program consists of two main scripts:
- `LibraryClasses.py` 
- `LibraryFunctions.py`

In this architecture: 

`LibraryClasses` acts defines the classes and functions of the library, i.e. saviving and searching for books. The script also defines the data structure of a book, and provides other background definintions.

`LibraryFunctions` provides the main functionality of the user-facing application, i.e. doing the adding, finding, and removing books. It uses the classes defined in `LibraryClasses` to interact with the library data to complete these various operations.

## Usage
To use the library manager, run `LibraryFunctions.py`.
