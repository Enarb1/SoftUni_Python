looking_for_this_book = input()

books_checked = 0

while True:
    command = input()
    if command == "No More Books":
        print("The book you search is not here!")
        print(f"You checked {books_checked} books.")
        break

    if command == looking_for_this_book:
        print(f"You checked {books_checked} books and found it.")
        break

    books_checked += 1
