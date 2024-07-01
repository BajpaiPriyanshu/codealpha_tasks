import random

def select_word():
    words = ["python", "hangman", "programming", "developer", "algorithm", "function", "variable"]
    return random.choice(words)

def display_current_state(word, guessed_letters):
    display_word = ''.join([letter if letter in guessed_letters else '_' for letter in word])
    return display_word

def hangman():
    word = select_word()
    guessed_letters = set()
    incorrect_guesses = 0
    max_incorrect_guesses = 6

    print("Welcome to Hangman!")
    print(f"The word has {len(word)} letters.")

    while incorrect_guesses < max_incorrect_guesses:
        current_state = display_current_state(word, guessed_letters)
        print(f"Current state: {current_state}")
        print(f"Incorrect guesses: {incorrect_guesses}/{max_incorrect_guesses}")

        guess = input("Guess a letter: ").lower()
        if guess in guessed_letters:
            print("You've already guessed that letter. Try again.")
        elif guess in word:
            guessed_letters.add(guess)
            print(f"Good guess! The letter '{guess}' is in the word.")
        else:
            guessed_letters.add(guess)
            incorrect_guesses += 1
            print(f"Wrong guess. The letter '{guess}' is not in the word.")

        if all(letter in guessed_letters for letter in word):
            print(f"Congratulations! You've guessed the word: {word}")
            break
    else:
        print(f"Sorry, you've run out of guesses. The word was: {word}")

if __name__ == "__main__":
    hangman()
