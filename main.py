from stats import count_words
from stats import chara_times
from stats import sorting

def get_book_text(path_file):
    with open(path_file) as f:
        book_content = f.read()
    return book_content

def main():
    book_content = get_book_text("books/frankenstein.txt")
    wrd = count_words(book_content)
    chara = chara_times(book_content)
    m = sorting(chara)
    print (f"============ BOOKBOT ============ ")
    print (f"Analyzing book found at books/frankenstein.txt...")
    print (f"----------- Word Count ----------")
    print (f"Found {wrd} total words")
    print (f"--------- Character Count -------")
    for i in m:
        if i["char"].isalpha():
            print (f"{i['char']}: {i['num']}")
    print (f"============= END ===============")
main()