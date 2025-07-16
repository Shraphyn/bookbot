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

def sort_on(items):
    return items["num"]
def sorting(dictio):
    list = []
    for entry in dictio:
            list.append({"char": entry, "num": dictio[entry]})
    list.sort(reverse=True, key=sort_on)
    return list
    

    