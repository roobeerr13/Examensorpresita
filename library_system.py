from enum import Enum

# Clase Enumerada BookGenre
class BookGenre(Enum):
    FICTION = "Fiction"
    NONFICTION = "Nonfiction"
    SCIENCE = "Science"
    ART = "Art"

    def __str__(self):
        return self.value

# Clase Book
class Book:
    def __init__(self, title: str, author: str, genre: BookGenre):
        """
        Inicializa un objeto Book con título, autor, género y estado.
        
        Args:
            title (str): Título del libro.
            author (str): Autor del libro.
            genre (BookGenre): Género del libro.
        """
        self._title = title
        self._author = author
        self._genre = genre
        self._is_borrowed = False  # False significa disponible

    # Getters
    @property
    def title(self) -> str:
        return self._title

    @property
    def author(self) -> str:
        return self._author

    @property
    def genre(self) -> BookGenre:
        return self._genre

    @property
    def is_borrowed(self) -> bool:
        return self._is_borrowed

    # Setters
    @title.setter
    def title(self, title: str):
        if not title.strip():
            raise ValueError("El título no puede estar vacío")
        self._title = title

    @author.setter
    def author(self, author: str):
        if not author.strip():
            raise ValueError("El autor no puede estar vacío")
        self._author = author

    @genre.setter
    def genre(self, genre: BookGenre):
        if not isinstance(genre, BookGenre):
            raise ValueError("El género debe ser un valor de BookGenre")
        self._genre = genre

    @is_borrowed.setter
    def is_borrowed(self, status: bool):
        self._is_borrowed = status

    # Método is_available
    def is_available(self) -> bool:
        """
        Verifica si el libro está disponible.

        Returns:
            bool: True si el libro está disponible, False si está prestado.
        """
        return not self._is_borrowed

    def __str__(self) -> str:
        """
        Representación en cadena del libro.

        Returns:
            str: Información del libro.
        """
        status = "Disponible" if self.is_available() else "Prestado"
        return f"Título: {self._title}, Autor: {self._author}, Género: {self._genre}, Estado: {status}"


# Ejemplo de uso (para pruebas)
if __name__ == "__main__":
    # Crear un libro
    book = Book("1984", "George Orwell", BookGenre.FICTION)
    print(book)  # Imprimir información del libro
    print(f"¿Está disponible? {book.is_available()}")  # Verificar disponibilidad

    # Cambiar estado a prestado
    book.is_borrowed = True
    print(book)
    print(f"¿Está disponible? {book.is_available()}")

    # Probar setters
    book.title = "Animal Farm"
    book.author = "G. Orwell"
    book.genre = BookGenre.FICTION
    print(book)