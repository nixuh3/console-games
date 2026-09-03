import random


def play():
    attempts_left = 10
    min_limit = 1
    max_limit = 1000
    secret_number = random.randint(min_limit, max_limit)

    print(f"Welcome to 'Guess the Number'! You have {attempts_left} attempts.")

    while True:
        guess_str = (
            input(
                f"\nTry to guess a number between {min_limit} and {max_limit} inclusive ('q' to quit): "
            )
            .strip()
            .lower()
        )

        if guess_str == "q":
            break

        try:
            guess = int(guess_str)
        except ValueError:
            print("Invalid input. Please enter a whole number.")
            continue

        if not (min_limit <= guess <= max_limit):
            print(
                f"Out of bounds! The number can only be between {min_limit} and {max_limit}... "
                f"That was way too {'big' if guess > max_limit else 'small'}!"
            )
            continue

        attempts_left -= 1

        if guess == secret_number:
            print(f"Congratulations! You guessed the correct number ({secret_number})!")
            break

        if attempts_left == 0:
            print(
                f"\nNo!!! You ran out of attempts! The number was {secret_number}. Better luck next time!"
            )
            break

        if guess > secret_number:
            print(f"That was too big! You have {attempts_left} attempts left.")
            max_limit = guess - 1
        else:
            print(f"That was too small! You have {attempts_left} attempts left.")
            min_limit = guess + 1

    print("Thanks for playing 'Guess the Number'.")


if __name__ == "__main__":
    play()
