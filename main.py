def main():
    def sort_on(dict):
        return dict["num"]
    
    char_dict = count_characters()
    char_list = [{"char": char, "num": count} for char, count in char_dict.items()]
    char_list.sort(reverse=True, key=sort_on)
    
    count = count_words()
    
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{count} words found in the document\n")
    for char_info in char_list:
        char = char_info['char']
        count = char_info['num']
        if char.isalpha():  # Only print alphabetic characters
            print(f"The '{char}' character was found {count} times")
    print("--- End report ---")
        
def count_words():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        words = file_contents.split()
        count = 0
        for w in words:
            count += 1
        return count
        
def count_characters():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read().lower()
        words = file_contents.split()
        # Split words into characters
        # Count characters
        character_dict = {}
        count = 0
        for word in words:
            word_string = ''.join(word)
            for character in word_string:
                character_dict[character] = character_dict.get(character, 0) + 1
        return character_dict
    
main()