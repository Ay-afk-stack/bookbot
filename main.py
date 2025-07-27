import sys
from stats import get_num_words,get_num_characters,  get_sorted_list

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    path_to_book = sys.argv[1]
    get_book_text(path_to_book)


def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        num_words = get_num_words(file_contents)
        num_chars = get_num_characters(file_contents)
        sorted_dict = get_sorted_list(num_chars)
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {path_to_file}")
        print("----------- Word Count ----------")        
        print(f"Found {num_words} total words")
        print("--------- Character Count -------")
        for single_dict in sorted_dict:
            if single_dict['char'].isalpha():
                print(f"{single_dict['char']}: {single_dict['num']}") 
        
        
main()