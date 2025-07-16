from stats import count_words
from stats import chara_times
from stats import sorting
import sys

def get_book_text(path_file):
    with open(path_file) as f:
        book_content = f.read()
    return book_content

def main():
    path_file = sys.argvz
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book_content = get_book_text(path_file[1])
        wrd = count_words(book_content)
        chara = chara_times(book_content)
        m = sorting(chara)
        print (f"============ BOOKBOT ============ ")
        print (f"Analyzing book found at {path_file[1]}")
        print (f"----------- Word Count ----------")
        print (f"Found {wrd} total words")
        print (f"--------- Character Count -------")
        for i in m:
            if i["char"].isalpha():
                print (f"{i['char']}: {i['num']}")
        print (f"============= END ===============")
main()