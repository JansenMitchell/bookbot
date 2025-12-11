def count_words(book_text):
    num_words = 0
    text_split = book_text.split()
    for word in text_split:
        num_words += 1
    return num_words
