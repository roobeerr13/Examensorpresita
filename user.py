from book import Book

class User:
    def __init__(self, name: str):
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book: Book):
        if book.is_available():
            book.set_available(False)
            self.borrowed_books.append(book)
            print(f"{self.name} ha tomado prestado '{book.get_title()}'")
        else:
            print(f"Lo siento, '{book.get_title()}' no está disponible.")

    def return_book(self, book: Book):
        if book in self.borrowed_books:
            book.set_available(True)
            self.borrowed_books.remove(book)
            print(f"{self.name} ha devuelto '{book.get_title()}'")
        else:
            print(f"{self.name} no tiene '{book.get_title()}' prestado.")

    def get_borrowed_books(self):
        return [book.get_title() for book in self.borrowed_books]