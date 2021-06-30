


# Laura Nuñez - CS 241 - BYU -Idaho 
# Week 2 
# W02 Prepare: Checkpoint A
# Task:Demonstrate use of function parameters and return values.
# Purpose:Correctly use files and functions to solve problems.



def prompt_number():

   n = int(input("Please enter a positive number: "))
   while n < 0:
    print("Invalid entry, The number must be positive.")
    n=int(input("Enter a positive number:"))
    pass 
   print()
   return n
         

def compute_sum(n1,n2,n3):
 return (n1 + n2 + n3)

def main():
    
   a = prompt_number()
   b = prompt_number()
   c = prompt_number()
   
   sum = compute_sum(a, b, c)
   
   print("The sum is: %d" % (sum))


if __name__ == "__main__":
   main()