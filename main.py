from stats import count_characters, count_words


def get_book_text(path_to_file):
    with open(path_to_file, "r") as file:
        return file.read()


def main():
    book_text = get_book_text("books/frankenstein.txt")
    word_count = count_words(book_text)
    character_count = count_characters(book_text)
    print(f"Found {word_count} total words")
    print(character_count)


main()
