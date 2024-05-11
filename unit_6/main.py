def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    """
    A function that tries to update the guessed letter.

    Args:
        letter_guessed (str): The letter being guessed.
        old_letters_guessed (list): List of letters guessed so far.

    Returns:
        bool: True if the letter was successfully added to the guessed letters list, False otherwise.
    """
    check_in = check_valid_input(letter_guessed, old_letters_guessed)

    if check_in:
        old_letters_guessed.append(letter_guessed.lower())
        return True
    
    print('X')
    old_letters_guessed = sorted(old_letters_guessed)
    print('-> '.join(old_letters_guessed))
    return False

def check_valid_input(letter_guessed, old_letters_guessed) -> bool:
    """
    A function that checks the validity of the input letter.

    Args:
        letter_guessed (str): The letter being guessed.
        old_letters_guessed (list): List of letters guessed so far.

    Returns:
        bool: False if the input is invalid, True otherwise.
    """
    err = err_check(letter_guessed)

    if err == "E1" or err == "E2" or err == "E3":
        return False
    elif letter_guessed.lower() in old_letters_guessed:
        return False
    else:
        return True


def err_check(s) -> str:
    """Checks if the input is valid.

    Checks if the input is a single letter (case insensitive). If it is,
    returns the lowercase version of that letter. If it is not a single
    letter, but is still valid (e.g. a single letter AND has a length of 1),
    returns "E1". If it has a length of 1, but is not a single letter,
    returns "E2". If it has a length greater than 1, returns "E3".

    Args:
        s (str): The input to check.

    Returns:
        str: One of the following: the lowercase version of the input if it is
            a single letter, "E1" if it is a single letter AND has a length of
            1, "E2" if it has a length of 1 but is not a single letter, or
            "E3" if it has a length greater than 1.
    """
    len_s = len(s)

    if(s.isalpha() and len_s == 1):
        return s.lower()
    elif(s.isalpha()):
        return "E1"
    elif(len_s == 1):
        return "E2"
    else:    
        return "E3"


def main():
    old_letters = ['a', 'p', 'c', 'f'] 
    print(try_update_letter_guessed('A', old_letters))
    print(try_update_letter_guessed('s', old_letters))
    print(try_update_letter_guessed('$', old_letters))
    print(try_update_letter_guessed('d', old_letters))
    print(old_letters)
    

if __name__ == '__main__':
    main()
