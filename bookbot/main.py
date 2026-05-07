import sys
from stats import get_num_words, get_num_char, get_report


def get_book_text(filepath: str):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents



def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    text = get_book_text(sys.argv[1])
    num_words = get_num_words(text)
    # print(f"Found {num_words} total words")
    num_char = get_num_char(text)
    # print(num_char)
    sorted = get_report(num_char)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print(f"----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print(f"--------- Character Count -------")
    for d in sorted:
        if d["char"].isalpha():
            print(f'{d["char"]}: {d["num"]}')
    print("============= END ===============")

main()