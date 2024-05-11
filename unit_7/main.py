def check_win(secret, guessed):
    """
    Checks if all the letters in the secret word are in the guessed letters.
    
    Args:
        secret (str): The secret word to be guessed.
        guessed (list): List of letters guessed so far.
    
    Returns:
        bool: True if all letters in the secret word are in the guessed letters, False otherwise.
    """
    return all(letter in guessed for letter in secret)


def show_hidden_word(secret_word, old_letters_guessed): 
    """
    A function that generates a string with spaces between each letter of the secret word if it has been guessed, and underscores otherwise.

    Args:
        secret_word (str): The word that needs to be guessed.
        old_letters_guessed (list): List of letters that have been guessed so far.

    Returns:
        str: A string representing the secret word with spaces between correctly guessed letters and underscores for letters that have not been guessed yet.
    """
    return ' '.join(c if c in old_letters_guessed else '_' for c in secret_word)

def main():
    secret_word = "yes"
    old_letters_guessed = ['d', 'g', 'e', 'i', 's', 'k', 'y'] 
    print(check_win(secret_word, old_letters_guessed)) 
    

if __name__ == '__main__':
    main()
