from microbit import *
import random

class Snake:
    """ This class contains the functions that operate
        on our game as well as the state of the game.
        It's a handy way to link the two.
    """

    def __init__(self):
        """ Special function that runs when you create
            a "Snake", ie. when you run
                game = Snake()
            init stands for "Initialisation"
        """
        #pass
        self.dc = "up"
        self.snake = [[0,1]]
        self.food = [2,2]
        #Direction coordinates
        self.end = False
        
        
        

    def handle_input(self):
        """ We'll use this function to take input from the
            user to control which direction the snake is going
            in.
        """
        #pass
        xc = accelerometer.get_x()
        yc = accelerometer.get_y()

        if abs(xc) >= abs(yc):
            if xc <= 0:
                self.dc = "left"
            if xc > 0:
                self.dc = "right" 
        else:
            if yc <= 0:
                self.dc = "up"
            if yc > 0:
                self.dc = "down"
        
       

    def update(self):
        """ This function will update the game state
            based on the direction the snake is going.
        """
        #pass
        
        new_head = [self.snake[-1][0], self.snake[-1][1]]
        if self.dc == "up":
            new_head[1] -= 1
        elif self.dc == "down":
            new_head[1] += 1
        elif self.dc == "right":
            new_head[0] += 1
        elif self.dc == "left":
            new_head[0] -= 1
            
        #self.end(new_head)
        if new_head in self.snake:
            self.end = True
        self.snake.append(self.bounds_accounted(new_head))
        
        if self.snake[-1] == self.food:
            self.foodeat()
            self.foodgen()
            
        self.snake = self.snake[1:]
        
        
        
        
    def bounds_accounted(self, cor):
        #new_head = self.snake[-1]
        if cor[1] < 0:
            cor[1] = 4
        if cor[0] < 0:
            cor[0] = 4
        if cor[1] > 4:
            cor[1] = 0
        if cor[0] > 4:
            cor[0] = 0
        return cor
        
    def foodgen(self):
        
        self.food = [random.randint(0, 4), random.randint(0, 4)]
        
        while self.food in self.snake:
            #self.snake.append(food)
            self.food = [random.randint(0, 4), random.randint(0, 4)]
            
        
            
    def foodeat(self):
        
            t = self.snake[0]
            if self.dc == "up":
                self.snake.insert(0, [t[0]+0, t[1]+1])
            elif self.dc == "down":
                self.snake.insert(0, [t[0]+0, t[1]-1])
            elif self.dc == "right":
                self.snake.insert(0, [t[0]+1, t[1]+0])
            elif self.dc == "left":
                self.snake.insert(0, [t[0]-1, t[1]+0])
            #t = self.snake[-1]
            #self.snake.append(([t[0]+1), (t[1]+1)]
    
            

    def draw(self):
        """ This makes the game appear on the LEDs. """
        display.clear()
        display.set_pixel(self.food[0], self.food[1], 9)
        for part in self.snake:
            display.set_pixel(part[0], part[1], 5)

# game is an "instance" of Snake
game = Snake()

# this is called our "game loop" and is where everything
# happens
while True:
    game.handle_input()
    game.update()
    if game.end:
        display.scroll('You lost')
        display.show(Image.SAD)
        break
    game.draw()
    # this makes our micro:bit do nothing for 500ms
    sleep(500)
