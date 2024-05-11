from unit_9.main import choose_word
from unit_8.main import hangman_status
from unit_7.main import check_win, show_hidden_word
from unit_6.main import try_update_letter_guessed, check_valid_input, err_check


TITLE = """
     _    _
    | |  | |
    | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __
    |  __  |/ _' | '_ \ / _' | '_ ' _ \ / _' | '_ \\
    | |  | | (_| | | | | (_| | | | | | | (_| | | | |
    |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                        __/  |
                        |___/ 
"""
MAX_TRIES = 6

def welcome_screen():
    """
    Welcome screen for Hangman game.

    Prints the ASCII art title and the welcome message to the user.

    """
    print(TITLE)


def get_words_path() -> tuple:
    """
    Get the path to the words file and the index of the word to be guessed.

    Asks the user for the path to the words file and the index of the word to be
    guessed. Returns a tuple of the path and the index.

    Returns:
        tuple: A tuple containing the path to the words file and the index of the word to be guessed.
    """
    while True:
        try:
            path = input("Enter path to words file: ")
            if not path:
                raise ValueError("Path cannot be empty.")
            index = int(input("Enter index: "))
            return path, index
            
        except ValueError as e:
            print(e)

def won():
    """
    Prints "WIN" and exits the program with a status code of 0.
    This function does not take any parameters and does not return anything.
    """
    print("WIN")
    exit(0)

def lost():
    """
    Prints "LOSE" and exits the program with a status code of 0.
    This function does not take any parameters and does not return anything.
    """
    print("LOSE")
    exit(0)

def main():
    """
    The main game loop.

    This function is the main game loop. It asks the user for input, updates the
    game state and prints the updated game state. It continues until the user
    has won or lost.
    """
    num_of_tries = 0  # Number of tries the user has made
    wrong_guesses = 0  # Number of wrong guesses the user has made

    welcome_screen()  # Print the welcome screen

    path, index = get_words_path()  # Get the path to the words file and the index of the word
    _, secret_word = choose_word(path, index)  # Get the word to be guessed
    old_letters_guessed = list()  # List of letters guessed by the user

    print("Let's start!")  # Print a starting message
    print(hangman_status(wrong_guesses))  # Print the current hangman status
    print(show_hidden_word(secret_word, old_letters_guessed))  # Print the hidden word

    while wrong_guesses < MAX_TRIES:  # While the user has not lost
        guess = input("Guess a letter: ").lower()  # Ask the user for input
        if not try_update_letter_guessed(guess, old_letters_guessed):  # If the input is invalid
            continue  # Continue the loop

        if guess not in secret_word:  # If the guess is not in the word
            wrong_guesses += 1  # Increment the number of wrong guesses
            print(":(")  # Print a disappointed message
            print(hangman_status(wrong_guesses))  # Print the updated hangman status

        print(show_hidden_word(secret_word, old_letters_guessed))  # Print the updated hidden word
        num_of_tries += 1  # Increment the number of tries

        if check_win(secret_word, old_letters_guessed):  # If the user has won
            won()  # Congratulate the user and exit

    lost()  # If the user has lost, print a message and exit


if __name__ == '__main__':
    main()
