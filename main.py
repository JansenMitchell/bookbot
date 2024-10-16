def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print(file_contents)
        
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
count_characters()