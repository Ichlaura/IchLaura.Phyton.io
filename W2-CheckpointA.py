
# Laura Nuñez - CS 241 - BYU -Idaho 
# Week 2 
# W02 Prepare: Checkpoint A
# Task:Demonstrate use of function parameters and return values.
# Purpose:Correctly use files and functions to solve problems.

#Tema.....................................................

print ("")
print ("Potential energy of a system")
print ("")


#Problema........................................................................

print ("Problem")
print("")
print ("A bowling ball held by a careless bowler slips from his hands and lands on his toe. If you choose the ground level as the point y 0 of your coordinate system, estimate the change in gravitational potential energy of the ball-Earth system as the ball falls. Repeat the calculation using the crown of the bowler's head as the origin of coordinates.")
print ("")

#Solución ........................................................................

print ("Answer")
print (" ")

#La energía potencial gravitacional del sistema bola– Tierra justo antes de que la bola de boliche se libere:
def potencia1(y1):
   h = m * g * y1
   return h

m = 7 #mass
g = 9.8  #gravedad 

result1 = potencia1(0.5)

print ( "The potential energy of the ball-ground system before being released:", round(result1))
print ("")

#La energía potencial gravitacional del sistema bola–Tierra cuando la bola llega al dedo del bolichista:
def potencia2(y2):
   h = m * g * y2
   return h

m = 7 #mass
g = 9.8  #gravedad 

result2 = potencia2(0.03)

print ("The potential energy of the ball-ground system when it reaches the bowler:", round(result2))
print ("")

#El cambio en energía potencial gravitacional del sistema bola–Tierra
x = result2 - result1
 

print ("The change in gravitational potential energy of the ball-Earth system:", round(x))
print ("")

#Blibliografía..........................................................................
# SERWAY -JEWETT, Física para ciencias e ingenierias, V1")
# Runestone Academy - Chapter 6
