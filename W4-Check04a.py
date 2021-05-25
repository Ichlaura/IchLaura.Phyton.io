

# Laura Nuñez - CS 241 - BYU -Idaho 
# Week 4
# W03 Prepare : Checkpoint A
# Task: Demonstrate composition in Python
# Purpose:Write programs that correctly use object composition to solve problems.

#.......PERSON............
#clase para una persona que ocntiene un nombre y un año de nacimiento
class Person:
    name       = ""
    birth_year = 0

#initializer para la persona clase lamada anonymous y el año unknown
    def __init__(self,name="anonymous",birth_year="unknown"):
        self.name = name
        self.birth_year = birth_year

#se crea un método para mostrar  el nombre y año en formato  de la persona 
    def display(self):
        aut = ("{} (b. {})".format(self.name, self.birth_year))
        return (aut)


#..........BOOK............        
#se crea otra clase llamada Book que contiene el titulo, autor y editor
class Book:
    title     = ""
    author    = ""
    publisher = ""

#initializer for book class
    def __init__(self,title="untitled",author= "person",publisher="unpublished"):
        self.title     = title
        self.author    = author
        self.publisher = publisher
# method - display 
    def display_dos(self):
        print(self.title)
        print("Publisher:")
        print(self.publisher)
        print("Author:")
        print(self.author)
   #new book     
def main():
    person1 = Person()
    aa = person1.display()
    new_book = Book(author = aa)
    new_book.display_dos()
    
    print("\nPlease enter the following:")
    a = input("Name: ")
    b = input("Year: ")
    c = input("Title: ")
    d = input("Publisher: ")
    print()
    person2 = Person(a,b)
    aaa = (person2.display())
    new_book = Book(title=c, author=aaa,publisher=d)
    new_book.display_dos()

if __name__=="__main__":
    main()
