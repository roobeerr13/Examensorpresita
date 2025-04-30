import gradio as gr
from library import Library
from genre import BookGenre

# Instancia de la biblioteca
library = Library()

def add_book(title, author, genre):
    if genre.upper() in BookGenre.__members__:
        library.add_book(title, author, BookGenre[genre.upper()])
        return f"Libro '{title}' añadido correctamente."
    return "Género no válido. Usa FICTION, NONFICTION, SCIENCE, ART."

def add_user(name):
    library.add_user(name)
    return f"Usuario '{name}' registrado con éxito."

def borrow_book(user_name, book_title):
    user = next((u for u in library.users if u.name == user_name), None)
    book = library.find_book(book_title)

    if user and book:
        user.borrow_book(book)
        return f"Libro '{book_title}' prestado a {user_name}."
    return "Usuario o libro no encontrado."

def return_book(user_name, book_title):
    user = next((u for u in library.users if u.name == user_name), None)
    book = library.find_book(book_title)

    if user and book:
        user.return_book(book)
        return f"Libro '{book_title}' devuelto por {user_name}."
    return "Usuario o libro no encontrado."

def list_books():
    return "\n".join([f"{book.get_title()} - {'Disponible' if book.is_available() else 'Prestado'}" for book in library.books])

# Crear interfaz con Gradio
iface = gr.Interface(
    fn=[add_book, add_user, borrow_book, return_book, list_books],
    inputs=[
        ["text", "text", "text"],  # Entrada para añadir libros (Título, Autor, Género)
        "text",  # Entrada para añadir usuario (Nombre)
        ["text", "text"],  # Préstamo de libro (Usuario, Título)
        ["text", "text"],  # Devolución de libro (Usuario, Título)
        None  # Listado de libros (No requiere entrada)
    ],
    outputs=["text", "text", "text", "text", "text"],
    live=True,
    title="Sistema de Gestión de Biblioteca",
    description="Añade libros, registra usuarios, presta y devuelve libros en una biblioteca virtual."
)

iface.launch()