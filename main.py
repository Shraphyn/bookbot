from stats import count_words

def get_book_text(path_file):
    with open(path_file) as f:
        book_content = f.read()
    return book_content

def main():
    book_content = get_book_text("books/frankenstein.txt")
    wrd = count_words(book_content)
    word_count = f"{wrd} words found in the document"
    print (word_count)
main()