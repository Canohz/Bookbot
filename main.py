from stats import get_character_count, convert_to_list, sort_on, num_words
import sys
def get_book_text(books):
    with open(books) as f:
        file_contents = f.read()
        return file_contents

def main():
    print('============= BOOKBOT =============')
    if len(sys.argv) != 2:
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)
    books = sys.argv[1]
    print(f'Analyzing book found at {books}...')
    file_contents = get_book_text(books)
    wordnum = num_words(file_contents)
    number = get_character_count(file_contents)
    number = convert_to_list(number)
    number.sort(reverse=True, key=sort_on)
    print('----------- Word Count ----------')
    print(f'Found {wordnum} total words.')
    print('----------- Character Count ----------')
    for i in number:
        if i['char'].isalpha():
            print(f"{i['char']}: {i['num']}")
        else:
            continue
    print('============= END ===============')
main()