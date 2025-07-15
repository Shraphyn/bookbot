def count_words(book_content):
    return len(book_content.split())

def chara_times(text):
    n = text.lower()
    dic = {}
    for txt in n: 
        if txt in dic:
            dic[txt] += 1
        else:
            dic[txt] = 1
    return dic