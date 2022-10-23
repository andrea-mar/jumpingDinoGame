import pygame

# initialize pygame modules
pygame.init()

# STAGE
# set the stage/window dimentions
stage_width = 800
stage_hight = 300
stage_size = (stage_width, stage_hight)
# stage colour
blue = 0, 0, 255
# draw the stage on the screen
stage = pygame.display.set_mode(stage_size)

# GROUND
# ground colour
green = 0, 225, 0
# coordinates and dimensions for the ground
(left, top) = (0, stage_hight - 50)
(ground_width, ground_height) = (stage_width, 50)

# DINOSAUR
# coordinates for the starting position of the dinosaur
(dino_x, dino_y) = (20, 160)
# load the dinosaur image
dinosaur = pygame.image.load("dinosaur.png")
dinosaur = pygame.transform.scale(dinosaur, (100, 100))

# the code below will be executed repeatedly until the player closes/quits the game
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    # update background colour
    stage.fill(blue)
    # draw the ground
    pygame.draw.rect(stage, green, pygame.Rect(left, top, ground_width, ground_height))
    
    # JUMP - no physics
    keys = pygame.key.get_pressed()
    # moves dinosaur up but not beyond the screen limit
    if keys[pygame.K_SPACE] and dino_y > 0:
            dino_y = dino_y - 5
    # moves dinosaur down until it reaches the ground
    elif dino_y < 160:
        dino_y = dino_y + 5

    # update dinosaur on screen
    stage.blit(dinosaur, (dino_x, dino_y))

    # update the whole stage
    pygame.display.flip()
 