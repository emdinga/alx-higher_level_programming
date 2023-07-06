#!/usr/bin/python3

def text_indentation(text):
    """
    Prints a text with 2 new lines after each '.', '?', and ':'

    Args:
        text (str): The input text

    Returns:
        None

    Raises:
        TypeError: If text is not a string

    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    text = text.strip()  # Remove leading and trailing whitespaces

    punctuation_marks = ['.', '?', ':']

    # Iterate over the text character by character
    for char in text:
        print(char, end='')  # Print the character

        # Check if the character is a punctuation mark
        if char in punctuation_marks:
            print('\n\n', end='')  # Print 2 new lines


# Run the doctest
if __name__ == '__main__':
    import doctest
    doctest.testmod()

