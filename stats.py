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


def sort_on(items):
    return items["num"]


def sort_dict_list(characters):
    dict_list = []
    for char, count in characters.items():
        dict_list.append({"char": char, "num": count})
    dict_list.sort(key=sort_on, reverse=True)
    return dict_list
