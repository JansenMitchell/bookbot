from stats import count_words


def get_book_text(path_to_file):
    with open(path_to_file, "r") as file:
        return file.read()


def main():
    book_text = get_book_text("books/frankenstein.txt")
    count = count_words(book_text)
    print(f"Found {count} total words")


main()
