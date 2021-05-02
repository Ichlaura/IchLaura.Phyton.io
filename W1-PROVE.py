

# Laura Nuñez - CS 241 - BYU -Idaho 
# Week 1 
# W01 Prove: Assignment
# Task:Demonstrate knowledge of variables, conditionals, and loops in Python
# Purpose:Learn the basics of Python

import random
from random import randint
game = "yes"
print("Welcome to the number guessing game!")
the_seed_value = input("Enter random seed: ")
random.seed(the_seed_value)

while game.lower() == "yes":
num = random.randint(1, 100)

guess = int(input("\nPlease enter a guess: "))
i = 1

while guess != num:
i = i + 1

if guess < num:
print("Higher")

elif:
print("Lower")
guess = int(input("\nPlease enter a guess: "))
else:
print("Congratulations. You guessed it!")
print(f"It took you {i} guesses.")
game = input("\nWould you like to play again? (yes/no) ")

if game == "no":
print("Thank you. Goodbye.")