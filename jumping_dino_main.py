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

# JUMP - variables
jumping = False
y_gravity = 0.1
jump_height = 6
jump_velocity = jump_height

# CACTUS
# coordinates for the starting position of the cactus
(cactus_x, cactus_y) = (700, 190)
# load the cactus image
cactus = pygame.image.load('cactus.png')
cactus = pygame.transform.scale(cactus, (50, 70))

# the code below will be executed repeatedly until the player closes/quits the game
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    # update background colour
    stage.fill(blue)
    # draw the ground
    pygame.draw.rect(stage, green, pygame.Rect(left, top, ground_width, ground_height))
    
    # JUMP - simple physics
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        jumping = True
    
    if jumping == True:
        # move dino up when velocity is positive, and down when velocity is negative
        dino_y = dino_y - jump_velocity
        jump_velocity = jump_velocity - y_gravity
        # stop jumping when dino reaches the ground
        if jump_velocity < -jump_height:
            jumping = False
            jump_velocity = jump_height

    # update dinosaur on screen
    stage.blit(dinosaur, (dino_x, dino_y))
    # update cactus on screen
    stage.blit(cactus, (cactus_x, cactus_y))

    # update the whole stage
    pygame.display.flip()
 