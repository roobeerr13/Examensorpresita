from book import Book
from user import User

class Employee:
    def __init__(self, name: str):
        self.name = name

    def manage_book_availability(self, book: Book, status: bool):
        book.set_available(status)
        print(f"{self.name} ha actualizado la disponibilidad de '{book.get_title()}' a {'disponible' if status else 'no disponible'}.")

    def view_user_borrowed_books(self, user: User):
        books = user.get_borrowed_books()
        if books:
            print(f"{user.name} tiene prestados los siguientes libros: {', '.join(books)}")
        else:
            print(f"{user.name} no tiene libros prestados.")