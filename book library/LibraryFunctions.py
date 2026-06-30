# Run this script to start the library UI.
# The script provides a simple command-line interface for a library management system.
# See LibraryClasses.py for the data structure and LIBRARIAN class.
# See the notes.md file for more information.

# Import the BOOK and LIBRARIAN classes from LibraryClasses.py so they can be used in this script.
from LibraryClasses import BOOK, LIBRARIAN

# Create an instance of the LIBRARIAN class to manage the library.
librarian = LIBRARIAN()


# Define the main function to run the library UI and handle user interactions.
def main():
    LIBRARIAN()
    lib_ui()
    check_complete()


# Define the check_complete function to handle user interactions after the library UI is complete.
def check_complete():
    user_iteration = input(
        "Is there anything else I can help with? Press any key to start again or 'q' to exit the library:  "
    )
    if user_iteration.lower() != "q":
        return lib_ui()
    else:
        exit()


# Here we are going to start the interaction by asking what is required by the user
def lib_ui():
    welcome_msg = input(
        "Welcome to the Library, press 1 to add a book and 2 search for a book:  "
    )
    if welcome_msg == "1":
        return add_new_book()
    if welcome_msg == "2":
        return book_search()
    else:
        attempt_msg = input(
            "I didn't get that. To exit the Library, press q, or any other key to start again:  "
        )
        if attempt_msg.lower() == "q":
            exit()
        else:
            lib_ui()


# Submission of a book record
def add_new_book():
    while True:
        title = input("Please enter the book title:  ")
        genres = input("Please enter book genres (comma-separated): ").split(",")
        author = input("Please enter the book's author:  ")

        confirmation = input(f"Add {title} by {author} to the library? (y/n): ")
        if confirmation.lower() == "y":
            librarian.add_book(title=title, genres=genres, author=author)
        else:
            print("Book addition cancelled.")
        return check_complete()


# Search for a book by genre, title, or author
def book_search():
    search_term = input(
        "For genre, press 1. To search titles, press 2. For author search, press 3:  "
    )
    if search_term.lower() == "1":
        return genre_search()
    elif search_term.lower() == "2":
        return title_search()
    elif search_term.lower() == "3":
        return author_search()
    else:
        try_again_msg = input(
            "I didn't get that. To exit the Library, press q, or any other key to start again:  "
        )
        if try_again_msg.lower() == "q":
            exit()
        else:
            book_search()


# Search for books by genre
def genre_search():
    genre_input = input("Please enter a genre: ")
    genre_results(genre_input)


# Display the results of a genre search
def genre_results(genre_input):
    found_books = librarian.find_books_by_genre(genre_input)
    if found_books:
        for book in found_books:
            print(book)
    else:
        print("No books found in the genre:", genre_input)


# Search for books by title
def title_search():
    title_input = input("Please enter a title:  ")
    title_results(title_input)


# Display the results of a title search
def title_results(title_input):
    found_books = librarian.find_books_by_genre(title_input)
    if found_books:
        for book in found_books:
            print(book)
    else:
        print("No books found with the title:", title_input)


# Search for books by author
def author_search():
    author_input = input("Please enter an author:  ")
    author_results(author_input)


# Display the results of an author search
def author_results(author_input):
    found_books = librarian.find_books_by_genre(author_input)
    if found_books:
        for book in found_books:
            print(book)
    else:
        print("No books found with the title:", author_input)


# Entry point of the library UI
if __name__ == "__main__":
    main()
