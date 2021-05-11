

class Rational_number():
    def __init__(self):
        self.numerator = 0
        self.denominator = 1

    def display(self):
        if self.numerator > self.denominator:
            integer_division = self.numerator // self.denominator
            residue_division = self.numerator % self.denominator
            print ("{} {}/{}".format(integer_division, residue_division, self.denominator))
        else:
            print("{}/{}" .format(self.numerator, self.denominator))

    def prompt(self):
        self.numerator = int(input("Enter the numerator: "))
        self.denominator = int(input("Enter the denominator: "))

    def display_decimal(self):
        print (self.numerator/self.denominator)

    def reduce(self):
      a = 1
      for f in range(1,min(self.numerator, self.denominator)+1):
         if ((self.numerator % f == 0) and (self.denominator % f == 0)):
            a = f
      self.numerator //= a 
      self.denominator //= a

    def multiply_by(self, first_object):
       self.numerator *= first_object.numerator
       self.denominator *= first_object.denominator
        
              
def main():
  
    first_object = Rational_number()
    print("")
    first_object.display()
    print()
    first_object.prompt()

    print()
    first_object.display_decimal()
    print()

    first_object.reduce()
    first_object.display()
    input()

    print()
    second_object = Rational_number()
    second_object.prompt()
  
    print()
    first_object.multiply_by(second_object)
    first_object.display()
    first_object.reduce()
  

    

if __name__== "__main__":
    main()