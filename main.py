def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = get_word_count(text)
    letter_count = get_letter_count(text)
    print(f"Letter count: {letter_count}")


def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def get_word_count(text):
    return len(text.split())

def get_letter_count(text):
    # TODO: Split each word into letters and count them
    # TODO: Make each letter lowercase
    # TODO: Return the total count of letters in a dictionary
    letter_dict = {}
    
    for letter in text:
        if letter.isalpha():
            letter = letter.lower()
            if letter in letter_dict:
                letter_dict[letter] += 1
            else:
                letter_dict[letter] = 1
    return letter_dict
    
main()
