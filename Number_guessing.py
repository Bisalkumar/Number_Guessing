import random

def get_range_and_attempts(difficulty):
    if difficulty == "easy":
        return (1, 50, 10)
    elif difficulty == "medium":
        return (1, 100, 7)
    elif difficulty == "hard":
        return (1, 200, 5)

def guess_number():
    print("Welcome to the Number Guessing Game!")
    print("Choose a difficulty level: easy, medium, or hard")

    while True:
        difficulty = input("Enter difficulty: ").lower()
        if difficulty in ["easy", "medium", "hard"]:
            break
        else:
            print("Invalid difficulty level. Please choose: easy, medium, or hard")

    min_range, max_range, max_attempts = get_range_and_attempts(difficulty)
    secret_number = random.randint(min_range, max_range)
    attempts = 0

    print(f"I'm thinking of a number between {min_range} and {max_range}. Can you guess it?")

    while attempts < max_attempts:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You've guessed the number {secret_number} in {attempts} attempts.")
            break

    if attempts >= max_attempts:
        print(f"Sorry, you've run out of attempts. The secret number was {secret_number}.")

    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() == "yes":
        guess_number()
    else:
        print("Thank you for playing!")

if __name__ == "__main__":
    guess_number()
