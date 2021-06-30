

# Laura Nuñez - CS 241 - BYU -Idaho 
# Week 3
# W03 Prove: Assignment 
# Task: Use classes to solve a problem in Python
# Purpose:Write programs that correctly use classes and objects to solve problems


class Robot:
    def __init__(self):
        self.x_coordinate = 10
        self.y_coordinate = 10
        self.fuel_amount = 100

    def status(self):
        print ("({}, {}) - Fuel: {}".format
               (self.x_coordinate,self.y_coordinate, self.fuel_amount))
        
    def fire_laser(self):    
        if self.fuel_amount > 10:
            print("Pew! Pew!")
            self.fuel_amount = self.fuel_amount -15
        else:
            if self.fuel_amount <=10:
                print("Insufficient fuel to perform action")
            
    def prompt(self):
        play = "on"
        while (play == "on"):
            comand = str(input("Enter command: "))
            if (comand == "fire"):
                self.fire_laser()
            elif (comand == "status"):
                self.status()
            elif (comand == "left"):
                self.left()
            elif (comand == "right"):
                self.right()
            elif (comand == "up"):
                self.up()
            elif (comand == "down"):
                self.down()
            elif (comand == "quit"):
                self.quit()
                break
        pass
    

    def left(self):
        if self.fuel_amount > 0:
            self.x_coordinate = self.x_coordinate -1
            self.fuel_amount = self.fuel_amount -5
        else:
            if self.fuel_amount == 0:
                print("Insufficient fuel to perform action")
            
    def right(self):
        if self.fuel_amount > 0:
            self.x_coordinate = self.x_coordinate +1
            self.fuel_amount = self.fuel_amount -5
        else:
            if self.fuel_amount == 0:
                print("Insufficient fuel to perform action")
            
    def down(self):
        if self.fuel_amount > 0:
            self.y_coordinate = self.y_coordinate +1
            self.fuel_amount = self.fuel_amount -5
        else:
            if self.fuel_amount == 0:
                print("Insufficient fuel to perform action")
    def up(self):
        if self.fuel_amount > 0:
            self.y_coordinate = self.y_coordinate -1
            self.fuel_amount = self.fuel_amount -5
        else:
            if self.fuel_amount == 0:
                print("Insufficient fuel to perform action")

    def quit(self):
        print ("Goodbye.")
            
def main():
    robot1 = Robot()
    robot1.prompt()
    
if __name__== "__main__":
    main()
