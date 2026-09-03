import random


def get_secret_word(filepath):
    with open(filepath, "r") as file:
        words = file.read().splitlines()
    return random.choice(words).lower()


def play_hangman():
    secret_word = get_secret_word("assets/hangman_words.txt")
    progress = ["_"] * len(secret_word)

    guessed_letters = set()
    wrong_letters = []
    attempts_left = 10

    print(f"Welcome to 'Hangman'! You have {attempts_left} attempts.")

    while True:
        print(f"\nWord: {''.join(progress)}")

        # 1. Get and format input
        guess = input("Guess a letter ('0' to quit): ").strip().lower()
        if guess == "0":
            break

        # 2. Validate input
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single alphabetic letter.")
            continue

        # 3. Check for duplicates
        if guess in guessed_letters:
            print(f"You already guessed '{guess}'! Try another one.")
            continue

        guessed_letters.add(guess)

        # 4. Check if the guess is correct
        if guess in secret_word:
            print("Correct!")
            for i, letter in enumerate(secret_word):
                if letter == guess:
                    progress[i] = guess

            # Win condition: no more blanks
            if "_" not in progress:
                print(f"\nCongratulations! The word was '{secret_word}'.")
                break
        else:
            attempts_left -= 1
            wrong_letters.append(guess)
            print("Wrong!")
            print(f"You have {attempts_left} attempts left!")

            if wrong_letters:
                print(f"Wrong letters: {' '.join(wrong_letters)}")

            # Loss condition
            if attempts_left == 0:
                print(
                    f"\nNo!!! You ran out of attempts! The word was '{secret_word}'. Better luck next time!"
                )
                break

    print("Thanks for playing 'Hangman'.")


if __name__ == "__main__":
    play_hangman()
