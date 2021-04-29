

# Laura Nuñez - CS 241 - BYU -Idaho 
# Week 2 
# W02 Prepare: Checkpoint B
# Task: Demonstrate file reading
# Purpose:Correctly use files and functions to solve problems.
print("")
print ("The future of quantum computing and Artificial Intelligence")
print ("")
print ("Two orthogonal states of a subatomic particle")
print ("The particle can be in coherent superposition")
print("")

cuantum = open("quantum.txt", "r")
for aline in cuantum:
    values = aline.split()
    print( "Could be ",values[0], values[1], "Or Could be",values[2], values[3] )

cuantum.close()
print("")
print ("Quantum computing or quantum computing1 is a computing paradigm different from that of classical computing or classical computing. It is based on the use of qubits, a special combination of ones and zeros. Classic computing bits can be 1 or 0, but only one state at a time; while the qubits can have the two simultaneous states as well. This gives rise to new logic gates that make new algorithms possible.")
