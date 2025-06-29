from stats import word_count,count_letter,sort_dict
import sys




def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents

def main():

    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]

    words = get_book_text(book_path)
    total_words = word_count(words)
    dict_of_letters = count_letter(words)
    sorted_list = sort_dict(dict_of_letters)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    print(f"Found {total_words} total words")
    print("--------- Character Count -------")
    for val in sorted_list:
        if val['char'].isalpha():
            print(f"{val['char']}: {val['num']}")
    print("============= END ===============")

    # print(sys.argv)
main()