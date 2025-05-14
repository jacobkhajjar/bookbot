def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    count = count_words(text)
    print(f"{count} words found in the document")


def get_book_text(file):
    with open(file) as f:
        return f.read()


def count_words(text):
    list = text.split()
    return len(list)
       
    
main()