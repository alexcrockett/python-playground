"""
Inspiration from 'Doing Math With Python', No Starch Press, by Amit Saha.

This is a very simple program that finds the factors of a number. This is effectively done by iterating through all numbers from 1 to the user's number and checking if they are factors. This is implemented in a simple loop.
"""


# Collect input
def find_factors_input():
    users_query = input("Enter a whole number: ")
    # Validate input
    if users_query.isnumeric():
        users_number = int(users_query)
        find_factors(users_number)  # Call find_factors directly with the user's number
    else:
        print("Invalid input, try again.")


# Find factors of the user's number (iterate w. a for loop)
def find_factors(users_number):
    print(f"Factors of {users_number}:")
    for i in range(1, users_number + 1):
        if users_number % i == 0:
            print(i)  # Just print the factor


# Main loop to keep the program running until the user chooses to exit
def main():
    while True:
        find_factors_input()  # Get user input and find factors

        user_choice = input("Do you want to perform another calculation? (yes/no): ")
        if user_choice.lower() != "yes":
            print("Exiting program. Goodbye!")
            break  # Exit the loop, thus ending the program


if __name__ == "__main__":
    main()
