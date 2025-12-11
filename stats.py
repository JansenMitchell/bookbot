def count_words(book_text):
    num_words = 0
    text_split = book_text.split()
    for word in text_split:
        num_words += 1
    return num_words


def count_characters(book_text):
    characters = {}
    for character in book_text:
        character = character.lower()
        if character in characters:
            characters[character] += 1
        else:
            characters[character] = 1
    return characters
