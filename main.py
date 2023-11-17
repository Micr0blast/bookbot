


"""
    Opens a txt file and returns all the contents as string
    Accepts:
        path: str where path is relative or absolute

    Returns:
        book_contents: str 
"""
def read_book_from_txt(path: str) -> str:
    with open(path, 'r', encoding='utf8') as file:
        book_contents = file.read()

    return book_contents



"""
    Counts all letters in given string in lower case.
    Accepts:
        book: str where contents are some kind of unicode text
    Returns:
        count_dict: dict where each key is a letter and values are counts of letter
"""
def count_letters_in_book_content(book:str) -> dict:
    book_lower = book.lower()
    count_dict = dict()

    for letter in book_lower:
        if letter not in count_dict.keys():
            count_dict[letter] = 1
        else:
            count_dict[letter] += 1

    return count_dict



if __name__ == "__main__":
    # TODO add console kwargs option
    # TODO add whole directory analysis --dir path/to/books
    # TODO add single book analyis --book ./book_name
    # TODO add path option --path books/frankenstein.txt
    # How to differentiate between dir and path?

    dir = "books"
    book_name = 'frankenstein.txt'
    path = '/'.join([dir, book_name])


    book_contents: str = ''
    words: str = ''
    
    book_contents = read_book_from_txt(path)
    words = book_contents.split()
    word_count = len(words)
    letter_count = count_letters_in_book_content(book_contents)
    
    report_start = f'--- Begin report of {dir}/{book_name} ---'
    report_word_count = f'{word_count} found in book'
    report_character_count_template = "The character '{char}' was found {count} times"
    report_end = '--- End Report ---'

    print(report_start)
    print(report_word_count.ljust(len(report_word_count) + 4))
    
    letters_in_book = list(letter_count)
    letters_in_book.sort()

    for letter in letters_in_book:
        report_string = report_character_count_template.format(char=letter, count=letter_count[letter])
        print(report_string.ljust(len(report_string) +4))
    
    print(report_end)
