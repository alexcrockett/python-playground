# This script implements a simple rock-paper-scissors game
# It allows the user to make a choice and then the computer chooses a random option
# Players can play multiple rounds and choose to quit at any time
# It is a nice script to practice basic Python syntax and logic

# Import random module to generate computer's choice
import random

# Define the choices
rock = "ROCK"
paper = "PAPER"
scissors = "SCISSORS"

while True:
    # This line prompts the user to make a selection to begin the game
    prompt = input("Make a selection: rock, paper, or scissors \n")
    if prompt == "rock":
        prompt = rock
    elif prompt == "paper":
        prompt = paper
    else:
        prompt = scissors

    # This line prints the user's selection
    print(f"You chose: {prompt}")

    # This line generates the computer's selection
    comp_choices = [rock, paper, scissors]  # Define the computer's choices
    comp_selection = random.choice(
        comp_choices
    )  # Randomly select the computer's choice
    print(f"Computer chose: {comp_selection}")  # Print the computer's selection

    # Here the logic is defined to determine the winner
    final_selection = [
        prompt,
        comp_selection,
    ]  # Create a list of the user's and computer's selections
    win = [
        [rock, scissors],
        [paper, rock],
        [scissors, paper],
    ]  # Define the winning combinations

    # Results
    if comp_selection == prompt:
        print("It was a draw...try again")
    elif (
        final_selection == win[0]
        or final_selection == win[1]
        or final_selection == win[2]
    ):
        print("WOOT WOOT!You won!")
    else:
        print("You lost this round! Try again.")

    # Ask if the user wants to play again
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":  # If the user does not want to play again, exit the loop
        print("Thanks for playing!")
        break
