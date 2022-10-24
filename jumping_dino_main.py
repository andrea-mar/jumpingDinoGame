import pygame

# initialize pygame modules
pygame.init()
pygame.font.init()

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
dinorect = dinosaur.get_rect(center=(dino_x, dino_y))

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
cactus_speed = 2

# MESSAGES
# messages colour
white = 255, 255, 255
# create display for game over message
game_over_font = pygame.font.SysFont('Comic Sans MS', 30)
game_over_surface = game_over_font.render('', False, white)
(game_over_width, game_over_hight) = (stage_width/2 - 80, stage_hight/2 - 50)

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

    # collision detection
    dinorect = dinosaur.get_rect(center=(dino_x, dino_y))
    cactusrect = cactus.get_rect(center=(cactus_x,cactus_y))
    if pygame.Rect.colliderect(cactusrect, dinorect) == True:
        # stop moving the cactus
        cactus_speed = 0
        # stop the dinosaur from jumping
        jumping = False
        # show game over message
        game_over_surface = game_over_font.render('Game Over', False, white)
    
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

    # CACTUS MOVE RIGHT TO LEFT
    cactus_x = cactus_x - cactus_speed
    if cactus_x < -50:
        cactus_x = stage_width
    # update cactus on screen
    stage.blit(cactus, (cactus_x, cactus_y))
    # update game over message
    stage.blit(game_over_surface, (game_over_width, game_over_hight))

    # update the whole stage
    pygame.display.flip()
 