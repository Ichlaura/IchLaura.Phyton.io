

# Laura Nuñez - CS 241 - BYU -Idaho 
# Week 1 
# W01 Prove: Assignment
# Task:Demonstrate knowledge of variables, conditionals, and loops in Python
# Purpose:Learn the basics of Python

import random
from random import randint
print("Welcome to the number guessing game!")

seed = input("Enter random seed: ")
random.seed(seed)

game = "yes"
while(game == "yes"):
    num = random.randint(1,100)
    count=1
    print()
    guess = int(input('Please enter a guess: '))
    while(num != guess):
        if(num < guess):
            print("Lower")
            print()
        elif(num > guess):
            print("Higher")
            print()
        guess = int(input('Please enter a guess: '))
        count=count+1
    print("Congratulations. You guessed it!")
    print("It took you",count,"guesses.")
    print()
    game = str(input("Would you like to play again (yes/no)? "))
print("Thank you. Goodbye.")