# Spacewalk
# Written by masterchief-solo
# Adapted from Mission Python by Sean McManus

# set your variables
WIDTH = 800
HEIGHT = 600
player_x = 600
player_y = 350

# define the function draw() to draw the backdrop image on screen, top-left corner of screen
def draw():
    screen.blit(images.backdrop, (0, 0))
