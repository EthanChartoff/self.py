def hangman_status(num_of_tries): 
    """
    Returns the hangman status picture based on the number of tries.

    Parameters:
    - num_of_tries (int): The number of tries the user has made.

    Returns:
    - str: The hangman status picture corresponding to the number of tries.

    Raises:
    - KeyError: If the num_of_tries is not a valid key in the HANGMAN_PHOTOS dictionary.
    """
    # picture 1:
    image1 = "x-------x"
    # picture 2:
    image2 = """x-------x
|
|
|
|
|"""
    # picture 3:
    image3 = """x-------x
|       |
|       0
|
|
|"""
    # picture 4:
    image4 = """x-------x
|       |
|       0
|       |
|
|"""
    # picture 5:
    image5 = """x-------x
|       |
|       0
|      /|\\
|
|"""
    # picture 6:
    image6 = """x-------x
|       |
|       0
|      /|\\
|      /
|"""
    # picture 7:
    image7 = """x-------x
|       |
|       0
|      /|\\
|      / \\
|"""

    HANGMAN_PHOTOS = {
        0: image1,
        1: image2,
        2: image3,
        3: image4,
        4: image5,
        5: image6,
        6: image7
    }

    if num_of_tries not in HANGMAN_PHOTOS:
        raise KeyError(f"Invalid num_of_tries: {num_of_tries}")

    return HANGMAN_PHOTOS[num_of_tries]



def main():
    num_of_tries = 6
    print(print_hangman(num_of_tries)) 
    

if __name__ == '__main__':
    main()
