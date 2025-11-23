#def main():
#    with open("books/frankenstein.txt") as f:
#        file_contents = f.read()
#    
#    num_words = len(file_contents.split())
#
#    print(f"Found {num_words} total words")
#
#main()

from stats import get_num_words, get_char_dict, get_sorted_list_dict
import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def main():
    book_path = sys.argv[1] 
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_char_dict(text)

#    print(f"Found {num_words} total words")

#    print(chars_dict)

    sorted_list = get_sorted_list_dict(chars_dict)
    print_report(book_path,num_words,sorted_list)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def print_report(book_path,num_words,sorted_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for item in sorted_list:
        if item["char"].isalpha():
            print(f"{item["char"]}: {item["num"]}" )


    print("============= END ===============")

main()
