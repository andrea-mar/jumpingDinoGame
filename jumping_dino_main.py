import pygame

# initialize pygame modules
pygame.init()

# set the stage/window dimentions
stage_width = 600
stage_hight = 300
stage_size = (stage_width, stage_hight)
# stage colour
blue = 0, 0, 255
# draw the stage on the screen
pygame.display.set_mode(stage_size).fill(blue)
pygame.display.update()

# the code below will be executed repeatedly until the player closes/quits the game
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()


    
    


