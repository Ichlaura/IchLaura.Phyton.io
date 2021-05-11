

# Laura Nuñez - CS 241 - BYU -Idaho 
# Week 3
# W03 Prepare : Checkpoint A
#Task: Demonstrate basic classes in Python
#Purpose:Write programs that correctly use classes and objects to solve problems


    #Create a class for a student, that contains a first name, a last name, and un Id.
class Student:
    
    #Create an _init_function in my class that initializes the first name,last name, and id.
   
 def __init__(self):
    self.name = ""
    self.last = ""
    self.id = 0
        

    #Create a regular function called prompt_student that creates a new student objects 
def prompt_student():
    
    student_one = Student()
    student_one.name = input("Please enter your first name: ")
    student_one.last = input("Please enter your last name: ")
    student_one.id = int(input("Please enter your id number: "))
    return student_one


   #Create a regular function (not a member function) called display_student that accepts a student object, and displays its information in the following format: "id - FirstName LastName"
def display_student(xobject):
    print ()
    print ("Your information:")
    print ("{} - {} {}" .format(xobject.id, xobject.name, xobject.last ))
    
    #Calls the prompt_student function and saves the returned value in a variable called "user".
    #Pass the user object to the display_student function to be displayed.
def main():
    student_final = prompt_student()
    display_student(student_final)
    
if __name__ == "__main__":
    main()