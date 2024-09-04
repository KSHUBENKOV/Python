# Number Guessing Game

# Set the correct answer that the user needs to guess
answer = 5

# Ask the user to guess a number between 1 and 10
print("Please guess a number between 1 and 10: ")

# Read the user's guess and convert it to an integer
guess = int(input())

# Check if the user's guess is less than the answer
if guess < answer:
    # Inform the user to guess a higher number
    print("Please guess higher")

    # Read the new guess from the user
    guess = int(input())

    # Check if the new guess is correct
    if guess == answer:
        print("Well done, you guessed it!")
    else:
        print("Sorry, you have not guessed correctly.")

# Check if the user's guess is greater than the answer
elif guess > answer:
    # Inform the user to guess a lower number
    print("Please guess lower")

    # Read the new guess from the user
    guess = int(input())

    # Check if the new guess is correct
    if guess == answer:
        print("Well done, you guessed it!")
    else:
        print("Sorry, you have not guessed correctly.")

# If the initial guess is neither less than nor greater than the answer, it must be correct
else:
    print("You got it right on the first try!")
