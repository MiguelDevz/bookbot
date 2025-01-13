def main():
    book_path = "books/frankenstein.txt"
    text = print_book_text(book_path)
    words_num = words_in_str(text)
    print(f"{words_num} words found in the document")
    chars_dict = get_chars_dict(text)
    dict_list = convert_dict(chars_dict)
    dict_list.sort(reverse=True, key=sort_on)
    print(f"--- Begin report of {book_path} ---")
    print(print_report(dict_list))
    print()

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

def convert_dict(dict):
    list_of_dicts = [{"letter": k, "num": v} for k,v in dict.items()]
    return list_of_dicts

def sort_on(dict):
    return dict["letter"]

def print_report(list_of_dict):
    for dict in list_of_dict:
        k =dict["letter"]
        v =dict["num"]
        if(k.isalpha()):
            print(f"The {k} character was found {v} times")
    return print("--- End report ---")

main()