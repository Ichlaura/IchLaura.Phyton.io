# Laura Nuñez - CS 241 - BYU -Idaho 
# Week 1 
# Prepare: Checkpoint B 
# Task:Demonstrate input output and variable use in Python
# Purpose:Learn the basics of Python


# WELCOME TO QUIZ TO BASIC KINEMATICS
# Book: 1. General information-  Runestone Academy


print ("Hi! Welcome to learn Physic")
print ("Quiz 1")
print ("Kinematics - rectilinear motion")

print("-------------")

#  Book: 4.4. The for Loop¶- Runestone Academy

for answers in ["true", "false"]:
    print ("the answer could be", answers)


# PREGUNTAS : QUESTIONS
# Book: 2.8. Input -  Runestone Academy

print("-------------")
print("Questions")
print("-------------")



one = input("1.Is it called rectilinear motion, that whose trajectory is a straight line.? (true/false) ")
two = input ("2.Is a uniform rectilinear motion one whose velocity is constant, therefore the acceleration is zero.? (true/false)")
tres = input ("3.Is a uniformly accelerated motion one whose acceleration is NOT constant.?(true/false)")

#Respuestas: ANSWER
# Book:7.4. Conditional Execution: Binary Selection - Runestone Academy
# Book: and Learn Python, Part 6: Conditionals - Thinket

print("-------------")
print("Answers")
print("-------------")



if one == "true":
    a = 10
    print ("Good Job, 10 points")
else:
        a= 0
        print ("Sadly, 0 points")
        
if two == "true":
   b = 10
   print ("Good Job, 10 points")
else:
        b = 0
        print ("Sadly, 0 points")
if tres == "false":
    c = 10
    print ("Good Job, 10 points")
else:
        c = 0
        print ("Sadly, 0 points")

#SCORE 
# Book: 7. Selection - Runestone Academy

print("-------------")
print("Total Score")
print("-------------")

print ( a + b + c)