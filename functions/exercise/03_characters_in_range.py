def characters_range(char_1, char_2):
    """Returns a single string with all the characters
    between char_1 and char_2 by ASCII table,
    separated by a single space"""

    list_chars = []

    for char in range(ord(char_1) + 1, ord(char_2)):
        list_chars.append(chr(char))

    return " ".join(list_chars)


first_char = input()
second_char = input()

print(characters_range(first_char, second_char))
