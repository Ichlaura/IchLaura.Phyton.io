
# We're gonna create aclass Phone
class Phone:
    def __init__(self):
        #These are the atributes
        self.area_code = 0
        self.prefix = 0
        self.suffix = 0

    #We're gonna create a prompt_number method to various input 
    def prompt_number(self):
        self.area_code = int(input("Area Code: "))
        self.prefix = int(input("Prefix: "))
        self.suffix = int(input("Suffix: "))

    #We're gonna create a display_phone to to display the information
    def display_phone(self):
        print("Phone info:")
        print("({}){}-{}".format(self.area_code, self.prefix, self.suffix))

#We're gonna create a class SmartPhone 
class SmartPhone(Phone):
    #These are the atributes
    def __init__(self):
        Phone.__init__(self) 
        self.email = ""
        
    #We're gonna create a prompt method to call it
    def prompt(self):
        self.prompt_number()
        self.email = input("Email: ")

    #We're gonna create prompt method to call the method display_phone and display 
    def display(self):
        self.display_phone()
        print(self.email)

#We're gonna do a main  
def main():
    phone_one = Phone()
    print("Phone:")
    phone_one.prompt_number()
    print()
    phone_one.display_phone()
    print()
    smartphone_one = SmartPhone()
    print("Smart phone:")
    smartphone_one.prompt()
    print()
    smartphone_one.display()

if __name__ == "__main__":
    main() 