import sys
from stats import (
    get_num_words, 
    get_character_counts, 
    chars_dict_to_sorted_list)


def get_book_text(path_to_file: str) -> str:
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents


def print_report(path_to_file: str, num_words: int, sorted_char_counts_list: list[tuple[str, int]]) -> None:
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_file}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for ch in sorted_char_counts_list:
        if ch[0].isalpha():
            print(f"{ch[0]}: {ch[1]}")

    print("============= END ===============")


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    path_to_book = sys.argv[1]
    book_text = get_book_text(path_to_book)
    num_words = get_num_words(book_text)
    char_counts = get_character_counts(book_text)
    sorted_char_counts_list = chars_dict_to_sorted_list(char_counts)
    print_report(path_to_book, num_words, sorted_char_counts_list)


main()
