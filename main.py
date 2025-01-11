def main():
    book_path = "books/frankenstein.txt"
    text = print_book_text(book_path)
    print(text)
    words_num = words_in_str(text)
    print(f"{words_num} words found in the document")
    chars_dict = get_chars_dict(text)
    print(chars_dict)


def print_book_text(path):
    with open(path) as f:
        return f.read()
    
def words_in_str(str):
    words = str.split()
    return len(words)

def get_chars_dict(str):
    dict_count = {}
    for char in str:
        lowered_str = char.lower()
        if lowered_str in dict_count:
            dict_count[lowered_str] += 1
        else:
            dict_count[lowered_str] = 1
    return dict_count


main()