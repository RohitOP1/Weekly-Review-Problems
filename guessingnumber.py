import random

# User inputs the range
lower = int(input("Enter lower range: "))
upper = int(input("Enter upper range: "))

# Generate a random number within the range
guessed_no = random.randint(lower, upper)

chances = 10

while chances > 0:
    guess = int(input(f"Guess ({lower}-{upper}): "))

    if guess < lower or guess > upper:
        print(f"Enter a number between {lower} and {upper}.")
        continue  

    if guess == guessed_no:
        print(f"Correct! The number was {guessed_no}.")
        break  

    chances -= 1

if chances == 0:
    print(f"Game Over! The number was {guessed_no}.")
