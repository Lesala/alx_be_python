# The user has to guess a number between 1 and 15. The program tells them if they guessed too high, too low, or correctly.
import random # importing the random module to generate a random number
secret_number = random.randint(1, 15) # generating a random number between 1 and 15
guess = int(input("I'm thinking of a number between 1 and 15, can you guess it? ")) # prompting the user to guess a number
# comparing the user's guess with the secret number
match guess:
    case number if number < 1:
        if secret_number == guess:
            print("congradulations, you guessed it right!")
        else:
            print(" sorry, your guess is incorrrect.")
    case number:
        if guess > 15:
            print(" Sorry, you guess is out of range, try a lower number. ")

# Play again feature
play_again = input("Do you want to play again? (yes/no): ").strip().lower()
if play_again == 'yes':
    secret_number = random.randint(1, 15) # generating a new random number
else:
    print("Thanks for playing! Goodbye!")
    exit()
guess = int(input("I'm thinking of a number between 1 and 15, can you guess it? ")) # prompting the user to guess a number
match guess:
    case number:
        if secret_number == guess:
            print("congradulations, you guessed it right!")
        elif guess > 15:
            print(" Sorry, you guess is out of range, try a lower number. ")
        else:
            print(" sorry, your guess is incorrrect.")