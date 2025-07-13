def get_book_text(path_file):
    with open(path_file) as f:
        book_content = f.read()

    return book_content

def main():
    book_content = get_book_text("books/frankenstein.txt")
    print(book_content)

main()