class Book:
    def __init__(self, title, author, year):
        """Constructor: Initializes the book's title, author, and year"""
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        """Destructor: Prints a message when the book is deleted"""
        print(f"Deleting {self.title}")

    def __str__(self):
        """String representation: Returns a user-friendly format of the book details"""
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """Official representation: Returns a string that recreates the object"""
        return f"Book('{self.title}', '{self.author}', {self.year})"
