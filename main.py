import sys 
from stats import (
    word_count,
    char_dict,
    sort_dict,
    print_report
)

def get_books_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print(f"Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    #Books
    filepath = sys.argv[1]
    print(filepath)
    text = get_books_text(filepath)

    #Data Analisis
    num_words = word_count(text)
    char_num_dict = char_dict(text)
    sorted_dict = sort_dict(char_num_dict)

    #Print Report
    print_report(filepath, num_words, sorted_dict)
    

main()