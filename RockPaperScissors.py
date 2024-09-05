import random  # Import the random module to let the computer make random choices

choices = ["rock", "paper", "scissors"]  # The three possible choices for the game

# Start an infinite loop to keep the game running until the user decides to stop
while True:
    # Let the computer randomly pick rock, paper, or scissors
    computer_choice = random.choice(choices)

    # Ask the user for their choice and make sure it's in lowercase
    user_choice = input("Enter your choice (rock, paper, scissors): ").lower()

    # Check if the user's choice is valid (rock, paper, or scissors)
    if user_choice not in choices:
        print("Invalid choice. Please try again.")  # If not, prompt the user to try again
    else:
        # Print out both choices for clarity
        print(f"You chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")

        # Determine the outcome of the game
        if user_choice == computer_choice:
            print("It's a tie!")  # Both choices are the same
        elif (user_choice == "rock" and computer_choice == "scissors") or \
                (user_choice == "scissors" and computer_choice == "paper") or \
                (user_choice == "paper" and computer_choice == "rock"):
            print("You win!")  # User beats the computer
        else:
            print("Computer wins!")  # Computer beats the user

    # Ask the user if they want to play another round
    play_again = input("Do you want to play again? (yes/no): ").lower()

    # If the user types anything other than "yes," we break out of the loop
    if play_again != "yes":
        break

# After the loop ends, thank the user for playing
print("Thanks for playing!")
