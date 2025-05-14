from stats import count_words, count_characters

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = count_words(text)
    char_dict = count_characters(text)
    print(f"{word_count} words found in the document")
    print(char_dict)


def get_book_text(file):
    with open(file) as f:
        return f.read()
       
    
main()