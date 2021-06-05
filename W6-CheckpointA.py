

#Create a class for a Book that has the following member variables title,
#author, publication_year
class Book:
    def __init__(self):
        self.title = ""
        self.author = ""
        self.publication_year = 0
    # Creat prompt_book_info Method 
    def prompt_book_info(self):
        self.title = input("Title: ")
        self.author = input("Author: ")
        self.publication_year = int(input("Publication Year: "))

    # Creat display_book_info to show 
    def display_book_info(self):
        print()
        print("{} ({}) by {}".format(self.title, self.publication_year, self.author))
        
#create a class for a TextBook that extends a Book and adds the
#following member variable subject
class TextBook(Book):
    def __init__(self):
        Book.__init__(self)         
        self.subject = ""

    # Creat prompt_subject Method 
    def prompt_subject(self):
        self.subject = input("Subject: ")

    # Creat display_subject to show 
    def display_subject(self):
        print("Subject: {}".format(self.subject))  

#create a class for a PictureBook that that extends a Book
#and adds the following member variable illustrator
class PictureBook(Book):
    def __init__(self):
        Book.__init__(self)  
        self.illustrator = ""
        
    # Creat prompt_illustrator Method 
    def prompt_illustrator(self):
        self.illustrator = input("Illustrator: ")

    # Creat display_illustrator to show 
    def display_illustrator(self):
        print("Illustrated by {}".format(self.illustrator))


def main():
    book1= Book()
    book1.prompt_book_info()
    book1.display_book_info()
    print()
    textbook1 = TextBook()
    textbook1.prompt_book_info()
    textbook1.prompt_subject()
    textbook1.display_book_info()
    textbook1.display_subject()
    print()
    picturebook1 = PictureBook()
    picturebook1.prompt_book_info()
    picturebook1.prompt_illustrator()
    picturebook1.display_book_info()
    picturebook1.display_illustrator()

if __name__ == "__main__":
    main()