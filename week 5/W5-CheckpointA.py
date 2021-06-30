

import random

#Im gonna create a Ship class
class Ship:
    #Here is the atributes
    
    def __init__(self):
        self.x = 0
        self.y = 0
        self.dx = 0
        self.dy = 0

    #This draw method should output
    def draw(self):
        print("Drawing ship at ({}, {})".format(self.x, self.y))

    #The advance method should move the ship forward one unit in time.
    #This is accomplished by adding dx onto x, and dy onto y  
    def advance(self):
        self.x += self.dx
        self.y += self.dy

class Game:
    def __init__(self, dx, dy):
        self.ship = Ship()
        self.ship.dx = dx
        self.ship.dy = dy

    #Here lets go call the methods from class Ship
    def on_draw(self):
        self.ship.draw()

    #Here lets go call the methods from class Ship
    def update(self):
        self.ship.advance()


def main():
    

    seed = input("Enter a random seed: ")
    random.seed(seed)

    dx = random.randint(-4, 4)
    dy = random.randint(-4, 4)

    print("Starting the ship with velocity ({}, {})".format(dx, dy))

    game = Game(dx, dy)

    for i in range(20):
        game.update()
        game.on_draw()

if __name__ == "__main__":
    main()
