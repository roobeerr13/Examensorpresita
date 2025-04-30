from genre import BookGenre

class Book:
    def __init__(self, title: str, author: str, genre: BookGenre, available: bool = True):
        self.title = title
        self.author = author
        self.genre = genre
        self.available = available

    def get_title(self):
        return self.title

    def get_author(self):
        return self.author

    def get_genre(self):
        return self.genre

    def is_available(self):
        return self.available

    def set_available(self, status: bool):
        self.available = status