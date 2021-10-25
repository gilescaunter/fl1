import pygame

road = [(10,10),(500,10),(500,400),(10,400)]

# Define some colors
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)
BLUE     = (   0,   0, 255)

class Car:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.speed = 0

    def start(self):
        self.x = 10
        self.y = 10

    def changeSpeed(self,newSpeed):
        self.speed = newSpeed

    def moveIt(self):



pygame.init()

size = (700, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption('Flow 1')

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop

    # --- Game logic should go here

    # --- Drawing code should go here

    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(WHITE)

    pygame.draw.line(screen,BLACK, road[0],road[1])
    pygame.draw.line(screen, BLACK, road[1],road[2])
    pygame.draw.line(screen, BLACK, road[2], road[3])
    pygame.draw.line(screen, BLACK, road[3], road[0])

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)




