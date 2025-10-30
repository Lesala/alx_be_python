# Initiating the base class Book
class Book:
    """Base class representing a general book."""
    def __init__(self, title: str, author: str):
        self.title: str = title
        self.author: str = author

    def __str__(self) -> str:
        return f"{self.title} by {self.author}"


class EBook(Book):
    """Derived class representing an electronic book."""
    def __init__(self, title: str, author: str, file_size: int):
        super().__init__(title, author)  # Call the base class constructor
        self.file_size: int = file_size  # Unique to EBook

    def __str__(self) -> str:
        return f"{self.title} by {self.author} (EBook, {self.file_size}MB)"


class PrintBook(Book):
    """Derived class representing a printed book."""
    def __init__(self, title: str, author: str, page_count: int):
        super().__init__(title, author)  # Call the base class constructor
        self.page_count: int = page_count  # Unique to PrintBook

    def __str__(self) -> str:
        return f"{self.title} by {self.author} (PrintBook, {self.page_count} pages)"


class Library:
    """Class demonstrating composition by managing a collection of books."""
    def __init__(self):
        self.books: list[Book] = []  # Composition: Library has Books

    def add_book(self, book: Book) -> None:
        """Add a book (Book, EBook, or PrintBook) to the library."""
        self.books.append(book)

    def list_books(self) -> None:
        """Print details of each book in the library."""
        if not self.books:
            print("The library is empty.")
        else:
            print("Books in the library:")
            for book in self.books:
                print(f" - {book}")
