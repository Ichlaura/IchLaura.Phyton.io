#We're gonna Import these library 
import arcade
import math
import random

#Variables to window 
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 500

#Variables to object Rifle
RIFLE_WIDTH = 100
RIFLE_HEIGHT = 20
RIFLE_COLOR = arcade.color.BROWN

#Variables to bullets of the rifle 
BULLET_RADIUS = 3
BULLET_COLOR = arcade.color.BLACK_OLIVE
BULLET_SPEED = 10

#Variables to the target o enemy 
TARGET_RADIUS = 20
TARGET_COLOR = arcade.color.ORANGE
TARGET_SAFE_COLOR = arcade.color.BLUE
TARGET_SAFE_RADIUS = 15

#We're gonna do class point to settle it 
class Point():
    def __init__(self):
        """ Initialize Variables """
        self.x = 0
        self.y = 0
        
#We're gonna do class velocity to give velocity   
class Velocity():
    def __init__(self):#Initialize the atributes
        self.dx = 0
        self.dy = 0
        
class Bullet():
    
    def __init__(self):#Initialize the atributes 
        self.center = Point()
        self.velocity = Velocity()
        self.radius = BULLET_RADIUS
        self.angle = 45
        self.alive = True
        
    def advance(self):#Method to run the bullets 
        self.center.x += self.velocity.dx
        self.center.y += self.velocity.dy
        
    def draw(self):#Method to draw the bullets 
        arcade.draw_circle_filled(self.center.x, self.center.y, BULLET_RADIUS, BULLET_COLOR)
        
    def fire(self, angle: float):#Method to shoot the bullets
        self.velocity.dx = math.cos(math.radians(angle)) * BULLET_SPEED
        self.velocity.dy = math.sin(math.radians(angle)) * BULLET_SPEED
        
    def is_off_screen(self, SCREEN_WIDTH, SCREEN_HEIGHT):
        #Method to stablish parameters if bullets out over the window 
        if (self.center.x >= SCREEN_WIDTH) and (self.center.y <= 0):
            return True
        else:
            return False
        
        
class Target():
    
    def __init__(self):#Initialize atributes 
        self.center = Point()
        self.velocity = Velocity()
        self.radius = TARGET_RADIUS
        self.alive = True
        self.life = 1
        
    def advance(self):#Method to run the target 
        self.center.x += self.velocity.dx
        self.center.y += self.velocity.dy
        
    def is_off_screen(self, SCREEN_WIDTH, SCREEN_HEIGHT):
        #Method to stablish parameters if target out over the window 
        if (self.center.x >= SCREEN_WIDTH) or (self.center.y <= 0):
            return True
        else:
            return False

    
class Orange_Target(Target):
    def __init__(self):#Inherit  the atributes
        super().__init__()
    
    def draw(self):# Method to draw  the target
        arcade.draw_circle_filled(self.center.x, self.center.y, TARGET_RADIUS, TARGET_COLOR)
        
    def hit(self):
        self.alive = False
        return 1
        
            
class Number_Target(Target):
    def __init__(self):# Inherit atributes
        super().__init__()
        self.life = 3
        
    def draw(self):#Method to draw target 
        arcade.draw_circle_outline(self.center.x, self.center.y, self.radius, TARGET_COLOR)
        text_x = self.center.x - (self.radius / 2)
        text_y = self.center.y - (self.radius / 2)
        arcade.draw_text(repr(self.life), text_x, text_y, TARGET_COLOR, font_size = 20)
            
    def hit(self):# Method to handle hit 
        self.life -= 1
        if (self.life == 0):
            self.alive = False
            return 5
        elif (self.life == 1):
            return  1
        elif (self.life == 2):
            return  1
        
class Blue_Target(Target):
    def __init__(self):# Inherit Variables 
        super().__init__()
    
    def draw(self): # Method to draw target 
        arcade.draw_rectangle_filled(self.center.x, self.center.y, 40, 40, arcade.color.BLUE)
        
    def hit(self): # Method to handle hit 
        self.alive = False
        return -10

class Rifle():
    def __init__(self): # Initialize Variables 
        self.center = Point()
        self.center.x = 0
        self.center.y = 0
        self.angle = 45

    def draw(self): # Method to draw rifle 
        arcade.draw_rectangle_filled(self.center.x, self.center.y, RIFLE_WIDTH, RIFLE_HEIGHT, RIFLE_COLOR, 360-self.angle)

class Game(arcade.Window):
    """
    This class handles all the game callbacks and interaction
    It assumes the following classes exist:
        Rifle
        Target (and it's sub-classes)
        Point
        Velocity
        Bullet
    This class will then call the appropriate functions of
    each of the above classes.
    You are welcome to modify anything in this class, but mostly
    you shouldn't have to. There are a few sections that you
    must add code to.
    """

    def __init__(self, width, height):
        """
        Sets up the initial conditions of the game
        :param width: Screen width
        :param height: Screen height
        """
        super().__init__(width, height)

        self.rifle = Rifle()
        self.score = 0

        self.bullets = []
        self.targets = []


        arcade.set_background_color(arcade.color.WHITE)

    def on_draw(self):
        """
        Called automatically by the arcade framework.
        Handles the responsibility of drawing all elements.
        """

        # clear the screen to begin drawing
        arcade.start_render()

        # draw each object
        self.rifle.draw()

        for bullet in self.bullets:
            bullet.draw()

        for target in self.targets:
            target.draw()


        self.draw_score()

    def draw_score(self):
        """
        Puts the current score on the screen
        """
        score_text = "Score: {}".format(self.score)
        start_x = 10
        start_y = SCREEN_HEIGHT - 20
        arcade.draw_text(score_text, start_x=start_x, start_y=start_y, font_size=12, color=arcade.color.NAVY_BLUE)

    def update(self, delta_time):
        """
        Update each object in the game.
        :param delta_time: tells us how much time has actually elapsed
        """
        self.check_collisions()
        self.check_off_screen()

        # decide if we should start a target
        
        if (len(self.targets) == 0):
            if random.randint(1, 50) == 1:
                self.create_target()

        for bullet in self.bullets:
            bullet.advance()
        
        # TODO: Iterate through your targets and tell them to advance

        for target in self.targets:
            target.advance()

    def create_target(self):
        """
        Creates a new target of a random type and adds it to the list.
        :return:
        """
        random_target = random.randint(1 ,3)
        
        # TODO: Decide what type of target to create and append it to the list
        
        if random_target == 1:
            target = Orange_Target()
            target.velocity.dx = random.uniform(2,3)
            target.velocity.dy = random.uniform(-2, -3)
            target.center.y = random.uniform(500,700)
        
        elif random_target ==2:
            target = Number_Target()
            target.velocity.dx = random.uniform(1,1.5)
            target.velocity.dy = random.uniform(-1, -1.5)
            target.center.y = random.uniform(500,700)
        
        elif random_target == 3:
            target = Blue_Target()
            target.velocity.dx = random.uniform(2,3)
            target.velocity.dy = random.uniform(-2, -3)
            target.center.y = random.uniform(500,700)

        self.targets.append(target)
        

    def check_collisions(self):
        """
        Checks to see if bullets have hit targets.
        Updates scores and removes dead items.
        :return:
        """

        # NOTE: This assumes you named your targets list "targets"

        for bullet in self.bullets:
            for target in self.targets:

                # Make sure they are both alive before checking for a collision
                if bullet.alive and target.alive:
                    too_close = bullet.radius + target.radius

                    if (abs(bullet.center.x - target.center.x) < too_close and
                                abs(bullet.center.y - target.center.y) < too_close):
                        # its a hit!
                        bullet.alive = False
                        plus = target.hit()
                        self.score += plus
                        


                        # We will wait to remove the dead objects until after we
                        # finish going through the list

        # Now, check for anything that is dead, and remove it
        self.cleanup_zombies()

    def cleanup_zombies(self):
        """
        Removes any dead bullets or targets from the list.
        :return:
        """
        for bullet in self.bullets:
            if not bullet.alive:
                self.bullets.remove(bullet)

        for target in self.targets:
            if not target.alive:
                self.targets.remove(target)
    
    def check_off_screen(self):
        """
        Checks to see if bullets or targets have left the screen
        and if so, removes them from their lists.
        :return:
        """
        for bullet in self.bullets:
            if bullet.is_off_screen(SCREEN_WIDTH, SCREEN_HEIGHT):
                self.bullets.remove(bullet)

        for target in self.targets:
            if target.is_off_screen(SCREEN_WIDTH, SCREEN_HEIGHT):
                self.targets.remove(target)

    def on_mouse_motion(self, x: float, y: float, dx: float, dy: float):
        
        # set the rifle angle in degrees
        
        self.rifle.angle = self._get_angle_degrees(x, y)

    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        
        # Fire!
        
        angle = self._get_angle_degrees(x, y)

        bullet = Bullet()
        bullet.fire(angle)

        self.bullets.append(bullet)
        

    def _get_angle_degrees(self, x, y):
        """
        Gets the value of an angle (in degrees) defined
        by the provided x and y.
        Note: This could be a static method, but we haven't
        discussed them yet...
        """
        # get the angle in radians
        angle_radians = math.atan2(y, x)

        # convert to degrees
        angle_degrees = math.degrees(angle_radians)

        return angle_degrees

# Creates the game and starts it going
window = Game(SCREEN_WIDTH, SCREEN_HEIGHT)
arcade.run()