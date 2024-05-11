import errno, os

def choose_word(file_path, index):
    """
    Given a file path and an index, this function reads the contents of the file and returns the word at the specified index.

    The function first opens the file specified by file_path in read mode ('r') and reads the contents of the file into a list of words. If the file is not found, a FileNotFoundError is raised.

    Next, the function checks if the index is within the range of the list of words. If the index is not within the range, an IndexError is raised.

    Finally, the function returns the word at the specified index.

    Args:
        file_path (str): The path to the file containing the words.
        index (int): The index of the word to be returned.

    Returns:
        str: The word at the specified index.

    Raises:
        FileNotFoundError: If the file specified by file_path does not exist.
        IndexError: If the index is out of range.
    """
    # Check if file path is null or empty
    if not file_path:
        raise ValueError("File path is null or empty")

    # Check if index is negative
    if index < 0:
        raise ValueError("Index cannot be negative")

    # Open file in read mode
    try:
        with open(file_path, 'r') as f:
            words = f.read().split()
    # If file is not found, raise FileNotFoundError
    except (OSError, IOError) as e:
        if e.errno == errno.ENOENT:
            raise FileNotFoundError("File not found") from e
        raise

    # If file is empty, raise FileNotFoundError
    if not words:
        raise FileNotFoundError("File not found")

    # Check if index is within range of list of words
    if index >= len(words):
        raise IndexError("Index out of range")

    # Remove duplicates from list of words
    unique_words = set(words)

    # Return total number of unique words and the word at the specified index
    return (len(unique_words), words[index])



def main():
    print(choose_word("words.txt", 3)) 
    

if __name__ == '__main__':
    main()
