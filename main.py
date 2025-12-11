import sys

if len(sys.argv) != 2:
    print("Usage: python main.py <book_path>")
    sys.exit(1)

from stats import count_characters, count_words, sort_dict_list


def get_book_text(path_to_file):
    with open(path_to_file, "r") as file:
        return file.read()


def print_report(book_path, word_count, sorted_characters):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for item in sorted_characters:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")


def main():
    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    word_count = count_words(book_text)
    character_count = count_characters(book_text)
    sorted_characters = sort_dict_list(character_count)
    print_report(book_path, word_count, sorted_characters)


main()
