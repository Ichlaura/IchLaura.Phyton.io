

# Laura Nuñez - CS 241 - BYU -Idaho 
# Week 2 
# W02 Prepare: Checkpoint B
# Task: Demonstrate file reading
# Purpose:Correctly use files and functions to solve problems.


def get():
    
   file = input("Enter file: ")
   return file

def read(file):
    
   file_read = open(file, "r")
   
   count_line = 0 
   count_word = 0
   
   for line in file_read:
       
      count_line += 1
      words = line.split()     
      count_word += len(words)
      
   file_read.close()
   
   return (count_word, count_line)


def main():
    
   file = get()
   
   (count_word, count_line) = read(file)
   print("The file contains %d lines and %d words." %(count_line, count_word))

if __name__ == "__main__":
   main()