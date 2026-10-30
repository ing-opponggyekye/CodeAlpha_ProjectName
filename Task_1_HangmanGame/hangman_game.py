import random

# ASCII visual stages for Hangman (0 to 6 incorrect guesses)
HANGMAN_PICS = [
    """
       +---+
       |   |
           |
           |
           |
           |
    =========
    """,
    """
       +---+
       |   |
      O   |
           |
           |
           |
    =========
    """,
    """
       +---+
       |   |
      O   |
      |    |
           |
           |
    =========
    """,
    """
       +---+
       |   |
      O   |
     /|    |
           |
           |
    =========
    """,
    """
       +---+
       |   |
      O   |
     /|\\   |
           |
           |
    =========
    """,
    """
       +---+
       |   |
      O   |
     /|\\   |
     /     |
           |
    =========
    """,
    """
       +---+
       |   |
      O   |
     /|\\   |
     / \\   |
           |
    =========
    """
]

# Predefined list of words for the game
WORD_LIST = [
    'python', 'developer', 'codealpha', 'internship', 'algorithm',
    'function', 'variable', 'database', 'computer', 'software',
    'program', 'keyboard', 'terminal', 'graphics', 'network'
]

def get_display_word(word, guessed_letters):
    """Returns the word representation with guessed letters and underscores."""
    return ' '.join([letter if letter in guessed_letters else '_' for letter in word])

def play_hangman():
    """Main game loop for Hangman."""
    word = random.choice(WORD_LIST).lower()
    guessed_letters = set()
    incorrect_guesses = 0
    max_incorrect = len(HANGMAN_PICS) - 1

    print("\n" + "=" * 45)
    print("      WELCOME TO CODEALPHA HANGMAN GAME!     ")
    print("=" * 45)
    print(f"Guess the word! You have {max_incorrect} incorrect attempts.")

    while incorrect_guesses < max_incorrect:
        print(HANGMAN_PICS[incorrect_guesses])
        print(f"Word: {get_display_word(word, guessed_letters)}")
        print(f"Guessed letters: {', '.join(sorted(guessed_letters)) if guessed_letters else 'None'}")
        print(f"Remaining incorrect attempts: {max_incorrect - incorrect_guesses}")
        
        guess = input("\nEnter a letter: ").strip().lower()

        # Input validation
        if len(guess) != 1 or not guess.isalpha():
            print(">> Invalid input. Please enter a single letter.")
            continue
        
        if guess in guessed_letters:
            print(f">> You already guessed '{guess}'. Try another letter.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print(f">> Good job! '{guess}' is in the word.")
            # Check win condition
            if all(letter in guessed_letters for letter in word):
                print(HANGMAN_PICS[incorrect_guesses])
                print("\n" + "*" * 45)
                print(f"  CONGRATULATIONS! You guessed the word: {word.upper()}!")
                print("*" * 45)
                break
        else:
            incorrect_guesses += 1
            print(f">> Sorry, '{guess}' is not in the word.")

    if incorrect_guesses == max_incorrect:
        print(HANGMAN_PICS[incorrect_guesses])
        print("\n" + "X" * 45)
        print(f"  GAME OVER! You ran out of attempts.")
        print(f"  The correct word was: {word.upper()}")
        print("X" * 45)

def main():
    while True:
        play_hangman()
        replay = input("\nWould you like to play again? (y/n): ").strip().lower()
        if replay not in ('y', 'yes'):
            print("\nThanks for playing CodeAlpha Hangman! Goodbye!")
            break

if __name__ == '__main__':
    main()
