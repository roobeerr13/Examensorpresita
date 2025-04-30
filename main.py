from library import Library
from genre import BookGenre

def main():
    library = Library()

    while True:
        print("\n--- Sistema de Gestión de Biblioteca ---")
        print("1. Añadir libro")
        print("2. Registrar usuario")
        print("3. Prestar libro")
        print("4. Devolver libro")
        print("5. Consultar disponibilidad de libros")
        print("6. Guardar estado y salir")
        
        choice = input("Seleccione una opción: ")

        if choice == "1":
            title = input("Título del libro: ")
            author = input("Autor del libro: ")
            genre = input("Género (FICTION, NONFICTION, SCIENCE, ART): ").upper()
            if genre in BookGenre.__members__:
                library.add_book(title, author, BookGenre[genre])
            else:
                print("Género no válido.")

        elif choice == "2":
            name = input("Nombre del usuario: ")
            library.add_user(name)

        elif choice == "3":
            user_name = input("Nombre del usuario: ")
            book_title = input("Título del libro: ")
            user = next((u for u in library.users if u.name == user_name), None)
            book = library.find_book(book_title)
            if user and book:
                user.borrow_book(book)
            else:
                print("Usuario o libro no encontrado.")

        elif choice == "4":
            user_name = input("Nombre del usuario: ")
            book_title = input("Título del libro: ")
            user = next((u for u in library.users if u.name == user_name), None)
            book = library.find_book(book_title)
            if user and book:
                user.return_book(book)
            else:
                print("Usuario o libro no encontrado.")

        elif choice == "5":
            library.list_books()

        elif choice == "6":
            library.save_state()
            print("Saliendo del sistema...")
            break

        else:
            print("Opción no válida, intente nuevamente.")

if __name__ == "__main__":
    main()