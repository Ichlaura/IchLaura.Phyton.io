# Laura Nuñez - CS 241 - BYU -Idaho 
# Week 2 
# W02 Prove: Homework - Data Structures
# Task: Articulate and perform Big-O analyses
# Purpose:Write programs that correctly use classes and objects to solve problems

def enter_file():
    filename = input("Please enter the data file /Users/laurapaolanunez/Documents/BYU/BYU - IDAHO/Computer programming/PYTHON/rates.csv: ")
    return filename

def extracting(filename):
    num_lines = 0
    total = 0
    
    with open(filename,"r") as file:
        file.readline()
        for i in file:
            num_lines += 1
            a = i.split(",")
            total += float((a[6]))
            pass
            

        file.close()
    print (num_lines)
    rate_average = total/num_lines
    print('')
    print("The average commercial rate is: {}" .format(rate_average))
    print('')
        
    
def high_low(filename):
    
    highest = ['name', 'zip', 'state', 0.0]
    lowest = ['name', 'zip', 'state', 0.10]
    
    with open(filename,"r") as f:

        next(f)
        text = f.readline()
        
        while text:
            
            b = text.split(",")
            dat = [b[2],b[0],b[3],float(b[6])]

            if dat[3] > highest[3] :
                highest = dat

            if dat[3] < lowest[3]:
                lowest = dat
            text = f.readline()
        f.close()
    print("The highest rate is:")
    print("{} ({}, {}) - ${}" .format(highest[0], highest[1], highest[2], highest[3]))
    print('')
    print("The lowest rate is:")
    print("{} ({}, {}) - ${}" .format(lowest[0], lowest[1], lowest[2], lowest[3]))
        
    
def main():
    filename = enter_file()
    extracting(filename)
    high_low(filename)
    
    

if __name__== "__main__":
    main()