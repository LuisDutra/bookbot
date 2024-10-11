def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    report = get_book_report(chars_dict)
    #print(chars_dict)

def sort_on(chars_dict):
    return chars_dict["num"]

def get_book_report(chars_dict):
    dicList = list(chars_dict.items())

    dicList.sort()

    for dic in dicList:
        print(dic)    

def get_num_words(text):
    words = text.split()
    return len(words)


def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()