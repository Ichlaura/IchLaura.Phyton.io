# Laura Nuñez - CS 241 - BYU -Idaho 
# Week 2 
# W03 Prepare : Checkpoint B
# Task:Demonstrate basic class methods (member functions) in Python
# Purpose:Write programs that correctly use classes and objects to solve problems



    #Create a class for a Complex number that has two member variables, "real" and "imaginary".
class Imaginary:


    #Create an initializer function for this class that sets each part to 0.
    def __init__(self):
     
        self.real = 0
        self.imaginary = 0
        pass
   
     #Create a prompt method
    def prompt_methods(self):
        self.real = input("Please enter the real part: ")
        self.imaginary = input("Please enter the imaginary part: ")
        pass


    #Create a display method
    def display(self):
        print ("{} + {}i".format(self.real,self.imaginary))
        pass
    pass


    #Then, in your main function you should create two new complex numbers. Display them (which should show 0 + 0i), prompt the user for each one, and display them again.    
def main():
 
    a = Imaginary() 
    b = Imaginary()
    
    print("The values are:")
    a.display()
    b.display()

    print()
    a.prompt_methods()

    print()
    b.prompt_methods()

    print ()
    print("The values are:")
    a.display()
    b.display()
    pass

if __name__ == "__main__":
    main()