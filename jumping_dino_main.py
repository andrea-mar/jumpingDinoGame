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
# coordinates for the starting position of the dinosaur
(dino_x, dino_y) = (20, 160)

# draw the stage on the screen
stage = pygame.display.set_mode(stage_size)

# load the dinosaur image
dinosaur = pygame.image.load("dinosaur.png")
dinosaur = pygame.transform.scale(dinosaur, (100, 100))


# the code below will be executed repeatedly until the player closes/quits the game
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    stage.fill(blue)
    # draw the ground
    pygame.draw.rect(stage, green, pygame.Rect(left, top, ground_width, ground_height))
    # update dinosaur on screen
    stage.blit(dinosaur, (dino_x, dino_y))
    # update the whole stage
    pygame.display.flip()
