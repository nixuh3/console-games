from wordfreq import top_n_list


def generate_hangman(n=500):
    common_words = top_n_list("en", n)
    hangman_words = [w for w in common_words if 5 <= len(w) <= 8 and w.isalpha()]
    hangman_words.sort()

    with open("assets/hangman_words.txt", "w") as file:
        file.write("\n".join(hangman_words))


def generate_wordle(n=500):
    common_words = top_n_list("en", n)
    wordle_words = [w for w in common_words if len(w) == 5 and w.isalpha()]
    wordle_words.sort()

    with open("assets/wordle_words.txt", "w") as file:
        file.write("\n".join(wordle_words))


if __name__ == "__main__":
    generate_hangman()
