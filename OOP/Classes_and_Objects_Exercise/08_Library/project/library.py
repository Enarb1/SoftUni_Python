from typing import List, Dict
from project.user import User


class Library:

    def __init__(self):
        self.user_records: List[User] = []  # [User (id, Name), User(id, Name]
        self.books_available: Dict[str: List[str]] = {}  # {"Steven King": ["book1", "book2"]..}
        self.rented_books: Dict[str: Dict[str: int]] = {}  # {"Branko": {"book4": 5, "book5": 30},....}

    def get_book(self, author: str, book_name: str, days_to_return: int, user: User) -> str:
        if book_name in self.books_available[author]:
            self.books_available[author].remove(book_name)
            user.books.append(book_name)

            self.rented_books[user.username] = self.rented_books.get(user.username, {})
            self.rented_books[user.username][book_name] = days_to_return

            return f"{book_name} successfully rented for the next {days_to_return} days!"

        for data in self.rented_books.values():
            if book_name in data:
                return f'The book "{book_name}" is already rented and will be available in {data[book_name]} days!'

    def return_book(self, author: str, book_name: str, user: User) -> str or None:

        if book_name not in self.rented_books[user.username]:
            return f"{user.username} doesn't have this book in his/her records!"

        del self.rented_books[user.username][book_name]
        user.books.remove(book_name)
        self.books_available[author].append(book_name)
