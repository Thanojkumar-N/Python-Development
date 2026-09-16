import random

# Generate a random number between 1 and 100
number = random.randint(1, 100)

print("Guess the number between 1 and 100!")

while True:
    guess = int(input("Enter your guess: "))

    if guess < number:
        print("Too low! Try again.")
    elif guess > number:
        print("Too high! Try again.")
    else:
        print("Congratulations! You guessed the correct number.")
        break