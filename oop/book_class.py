# initiating a class to represent a book
class Book:
    def __init__(self, title, author, year):
        """" The constructor method initializes the
          book with title, author, and year of publication """
        self.title : str  = title
        self.author : str = author
        self.year : int = year
    
    def __del__(self):
        """ The destructor method prints a message when
          the book instance is deleted """
        print(f"Deleting {self.title}")
    
    def __str__(self) -> str :
        """ The string method returns a user-friendly
        string representation of the book """
        return f"{self.title} by {self.author}, published in {self.year}"
    
    def __repr__ (self) -> str :
        """ The official string representation of the book
        that can be used to recreate the object """
        return f"Book('{self.title}', '{self.author}', {self.year})"
    





































    def __init__(self, title, author, year):
        """Constructor that initializes a Book instance"""
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        """Destructor that prints a message when a Book instance is deleted"""
        print(f"Deleting {self.title}")

    def __str__(self):
        """User-friendly string representation"""
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """Official string representation that can recreate the object"""
        return f"Book('{self.title}', '{self.author}', {self.year})"
