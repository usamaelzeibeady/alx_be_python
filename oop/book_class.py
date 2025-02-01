class Book:
    def __init__(self, title, author, year):
        """
        Constructor method to initialize a Book instance.
        
        :param title: The title of the book.
        :param author: The author of the book.
        :param year: The publication year of the book.
        """
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        """
        Destructor method that prints a message when a Book instance is deleted.
        """
        print(f"Deleting {self.title}")

    def __str__(self):
        """
        String representation of the Book instance.
        
        :return: A string in the format "(title) by (author), published in (year)".
        """
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """
        Official representation of the Book instance.
        
        :return: A string that would recreate the Book instance.
        """
        return f"Book('{self.title}', '{self.author}', {self.year})"