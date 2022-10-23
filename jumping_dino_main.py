import pygame

# initialize pygame modules
pygame.init()

# set the stage/window dimentions
stage_width = 800
stage_hight = 300
stage_size = (stage_width, stage_hight)
# stage colour
blue = 0, 0, 255
# ground colour
green = 0, 225, 0
# coordinates and dimensions for the ground
(left, top) = (0, stage_hight - 50)
(ground_width, ground_height) = (stage_width, 50)

# draw the stage on the screen
stage = pygame.display.set_mode(stage_size)


# the code below will be executed repeatedly until the player closes/quits the game
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    stage.fill(blue)
    # draw the ground
    pygame.draw.rect(stage, green, pygame.Rect(left, top, ground_width, ground_height))
    pygame.display.flip()
