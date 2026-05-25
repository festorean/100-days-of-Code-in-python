import random

print("Welcome to Number Guessing Project")
print("I'm thinking of a number between 1 and 100")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
if difficulty == 'easy':
    attempts = 10
elif difficulty == 'hard':
    attempts = 5
else:
    print("wrong input. Try again.")
    exit()
computer_guess = random.randint(1,100)

while attempts > 0:
    print(f"You have {attempts} attempts left")
    player_guess = int(input("Make a guess: "))
    if player_guess == computer_guess:
        print("You guessed the number!")
        break
    elif player_guess > computer_guess:
        print("Guess too high!")
    else:
        print("Guess too low!")
    attempts -= 1

if attempts == 0:
    print(f"You lose the number was {computer_guess}")
