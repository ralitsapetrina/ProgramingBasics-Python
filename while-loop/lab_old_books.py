book = input()
library_range = int(input())
counter = 0

while counter < library_range:
    book_search = input()
    if book == book_search:
        print(f'You checked {counter} books and found it.')
        break
    counter += 1

if not book == book_search:
    print('The book you search is not here!')
    print(f'You checked {library_range} books.')