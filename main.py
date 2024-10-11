def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    report = get_book_report(chars_dict)

    print("Beging report of: " + book_path)
    print(f"{num_words} words found in the document")

    for r in report:
        if r[0].isalpha():
            print(f"The letter {r[0]} was found {r[1]} times")

    print("--- End report ---")

def sort_on(chars_dict):
    return chars_dict["num"]

def get_book_report(chars_dict):
    
   return sorted(chars_dict.items(), key=lambda item: item[1], reverse=True)

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