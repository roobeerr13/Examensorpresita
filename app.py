import gradio as gr
from library import Library
from genre import BookGenre

# Instancia de la biblioteca
library = Library()

def library_system(action, param1="", param2="", param3=""):
    if action == "Añadir libro":
        if param3.upper() in BookGenre.__members__:
            library.add_book(param1, param2, BookGenre[param3.upper()])
            return f"Libro '{param1}' añadido correctamente."
        return "Género no válido. Usa FICTION, NONFICTION, SCIENCE, ART."
    
    elif action == "Añadir usuario":
        library.add_user(param1)
        return f"Usuario '{param1}' registrado con éxito."
    
    elif action == "Prestar libro":
        user = next((u for u in library.users if u.name == param1), None)
        book = library.find_book(param2)
        if user and book:
            user.borrow_book(book)
            return f"Libro '{param2}' prestado a {param1}."
        return "Usuario o libro no encontrado."
    
    elif action == "Devolver libro":
        user = next((u for u in library.users if u.name == param1), None)
        book = library.find_book(param2)
        if user and book:
            user.return_book(book)
            return f"Libro '{param2}' devuelto por {param1}."
        return "Usuario o libro no encontrado."
    
    elif action == "Listar libros":
        return "\n".join([f"{book.get_title()} - {'Disponible' if book.is_available() else 'Prestado'}" for book in library.books])
    
    return "Acción no válida."

# Creación de la interfaz en Gradio
iface = gr.Interface(
    fn=library_system,
    inputs=[
        gr.Dropdown(choices=["Añadir libro", "Añadir usuario", "Prestar libro", "Devolver libro", "Listar libros"], label="Selecciona una acción"),
        gr.Textbox(label="Parámetro 1 (Título o Nombre de usuario)", placeholder="Título del libro o nombre de usuario"),
        gr.Textbox(label="Parámetro 2 (Autor o Título del libro)", placeholder="Autor del libro o título del libro"),
        gr.Textbox(label="Parámetro 3 (Género del libro, si aplica)", placeholder="Género del libro (FICTION, NONFICTION, etc.)")
    ],
    outputs=gr.Textbox(label="Resultado"),
    title="Sistema de Gestión de Biblioteca",
    description="Selecciona una acción y proporciona los datos necesarios para gestionar la biblioteca."
)

iface.launch()