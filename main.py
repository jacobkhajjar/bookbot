from stats import count_words, count_characters, sort_characters


def main():
    book_path = "books/frankenstein.txt"
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


main()