from book import Book
from genre import BookGenre
from user import User
from employee import Employee

class Library:
    def __init__(self):
        self.books = []
        self.users = []

    def add_book(self, title: str, author: str, genre: BookGenre):
        book = Book(title, author, genre)
        self.books.append(book)
        print(f"Libro '{title}' añadido a la biblioteca.")

    def add_user(self, name: str):
        user = User(name)
        self.users.append(user)
        print(f"Usuario '{name}' registrado en la biblioteca.")

    def find_book(self, title: str):
        for book in self.books:
            if book.get_title().lower() == title.lower():
                return book
        return None

    def list_books(self):
        print("\nLista de libros disponibles en la biblioteca:")
        for book in self.books:
            status = "Disponible" if book.is_available() else "Prestado"
            print(f"- {book.get_title()} ({status})")

    def save_state(self):
        print("\nGuardando estado actual de la biblioteca...")
        # Aquí podrías agregar código para guardar en un archivo JSON o base de datos
        print("Estado guardado con éxito.")