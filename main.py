from stats import count_words, count_characters, sort_characters

import sys

def main():
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    word_count = count_words(text)
    char_dict = count_characters(text)
    char_count = sort_characters(char_dict)
    print_report(book_path, word_count, char_count)
    

def get_book_text(file):
    with open(file) as f:
        file_contents = f.read()
    return file_contents


def print_report(book_path, word_count, char_count):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for line in char_count:
        print(f"{line['char']}: {line['num']}")
    print("============= END ===============")

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    main()