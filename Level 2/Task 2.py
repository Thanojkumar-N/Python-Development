import random

# Get the range from the user
lower = int(input("Enter the lower limit: "))
upper = int(input("Enter the upper limit: "))

# Generate a random number within the specified range
number = random.randint(lower, upper)

print(f"\nGuess the number between {lower} and {upper}.")

while True:
    guess = int(input("Enter your guess: "))

    if guess < number:
        print("Too low! Try again.")
    elif guess > number:
        print("Too high! Try again.")
    else:
        print("Congratulations! You guessed the correct number.")
        break