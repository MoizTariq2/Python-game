""" 
I acknowledge the use of
Microsoft Copilot (version GPT-4, Microsoft, https://copilot.microsoft.com/)
to create the code in this file 

Guess the Number Game
---------------------
A simple text-based game where the player tries to guess a random number.
Includes input validation, replay option, and scoring system.
"""

import random


def play_game():
    """Plays one round of Guess the Number."""
    number_to_guess = random.randint(1, 100)
    attempts = 0

    print("\n🎲 Welcome to Guess the Number!")
    print("I'm thinking of a number between 1 and 100.")

    while True:
        # Validate user input
        try:
            guess = int(input("Enter your guess: "))
            if not 1 <= guess <= 100:
                print("⚠️ Please guess a number between 1 and 100.")
                continue
        except ValueError:
            print("❌ Invalid input! Please enter a valid number.")
            continue

        attempts += 1

        # Compare guess to target number
        if guess < number_to_guess:
            print("Too low! Try again.")
        elif guess > number_to_guess:
            print("Too high! Try again.")
        else:
            score = max(100 - (attempts - 1) * 10, 10)
            print(f"✅ Correct! You guessed it in {attempts} attempts.")
            print(f"🏆 Your score: {score} points.\n")
            break


def main():
    """Main loop allowing multiple rounds."""
    while True:
        play_game()
        again = input("Would you like to play again? (y/n): ").lower().strip()
        if again != "y":
            print("\n👋 Thanks for playing Guess the Number!")
            break


if __name__ == "__main__":
    main()



