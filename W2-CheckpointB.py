

# Laura Nuñez - CS 241 - BYU -Idaho 
# Week 2 
# W02 Prepare: Checkpoint B
# Task: Demonstrate file reading
# Purpose:Correctly use files and functions to solve problems.

cuantum = open("quantum.txt", "r")

for aline in cuantum:
    values = aline.split()
    print('QB ', values[0], values[1], 'had a rating of ', values[10] )

cuantum.close()