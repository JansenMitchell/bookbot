def get_book_text(path_to_file):
    with open(path_to_file, "r") as file:
        return file.read()


def count_words(book_text):
    num_words = 0
    text_split = book_text.split()
    for word in text_split:
        num_words += 1
    return num_words


def main():
    book_text = get_book_text("books/frankenstein.txt")
    count = count_words(book_text)
    print(f"Found {count} total words")


main()
