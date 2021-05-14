import pygame

# initialize the pygame
pygame.init()

#create the screen
screen = pygame.display.set_mode((800,600))

# Title and icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("ufo.png")
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load("player.png")
playerX = 370
playerY = 480
playerX_change = 0

def player(x, y):
    # we are drawing the player image on the screen
    screen.blit(playerImg, (x, y)) # setting the player image and related cordinates

# Game loop
running  = True
while running:
    # looping all the available events in python
    screen.fill((0,0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # if keystroke is pressed check weather its right or left
        if event.type == pygame.KEYDOWN:
            print("A keystroke is pressed")
            if event.key == pygame.K_LEFT:
                print("Left arrow key is pressed")
                playerX_change = -0.3
            if event.key == pygame.K_RIGHT:
                print("Right arrow key is pressed")
                playerX_change = 0.3
        if event.type == pygame.KEYUP:
            if event.type == pygame.KEYUP or event.key == pygame.K_RIGHT:
                playerX_change = 0
                print("Keystroke has been released")
                

    # RGB - R, G, B
    playerX += playerX_change

    # Below code 53 to 56 are for the boundaries for the play area
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    player(playerX, playerY)
    pygame.display.update() # we have to update the game window for any change in the code