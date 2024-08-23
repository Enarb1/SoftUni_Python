def check_book(books_lst, index):
    if 0 <= index < len(books_lst):
        book_name = books_lst[index]
        print(book_name)
        return True
    return False


def insert_book(books_lst, book_name):
    if book_name not in books_lst:
        books_lst.append(book_name)


def swap(books_lst, book1, book2):
    if book1 in books_lst and book2 in books_lst:
        for idx, book in enumerate(books_lst):
            if book == book1:
                book_one_index = idx
            if book == book2:
                book_two_index = idx
                books_lst[book_one_index], books_lst[book_two_index] = books_lst[book_two_index],books_lst[book_one_index]


def take_books(books_lst, book_name):
    if book_name in books_lst:
        books_lst.remove(book_name)


def add_book(books_lst, book_name):
    if book_name not in books_lst:
        books_lst.insert(0,book_name)

def process_commands(books_lst, commands):
    for command in commands:
        command_parts = command.split(" | ")
        if command_parts[0] == "Add Book":
            book_name = command_parts[1]
            add_book(books_lst, book_name)
        elif command_parts[0] == "Take Book":
            book_name = command_parts[1]
            take_books(books_lst,book_name)
        elif command_parts[0] == "Swap Books":
            book_one = command_parts[1]
            book_two = command_parts[2]
            swap(books_lst, book_one, book_two)
        elif command_parts[0] == "Insert Book":
            book_name = command_parts[1]
            insert_book(books_lst, book_name)
        elif command_parts[0] == "Check Book":
            index = int(command_parts[1])
            check_book(books_lst, index)
    return books_lst


bookshelf = input().split("&")
commands_list = []
while True:
    cmnd = input()
    if cmnd == "Done":
        break
    commands_list.append(cmnd)
process_commands(bookshelf, commands_list)
print(", ".join(bookshelf))