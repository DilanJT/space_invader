import pygame
import random

# initialize the pygame
pygame.init()

#create the screen
screen = pygame.display.set_mode((800,600))

#background
background = pygame.image.load("background.jpg")

# Title and icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("ufo.png")
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load("player.png")
playerX = 370
playerY = 480
playerX_change = 0

#setting up the enemy
enemyImg = pygame.image.load("enemy.png")
enemyX = random.randint(0, 800)
enemyY = random.randint(50, 150)
enemyX_change = 0.3
enemyY_change = 40

#setting up the bullet
# Bullet states
# Ready - You cant see the bullet on the screen
# Fire - The bullet is currently moving
bulletImg = pygame.image.load("bullet.png")
bulletX = 0
bulletY = 480 # at the position of the spaceship
bulletX_change = 0
bulletY_change = 1
bullet_state = "ready"

# function to locate the player
def player(x, y):
    # we are drawing the player image on the screen
    screen.blit(playerImg, (x, y)) # setting the player image and related cordinates

# Function to locate the enemy
def enemy(x, y):
    # we are drawing the player image on the screen
    screen.blit(enemyImg, (x, y)) # setting the player image and related cordinates

def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10)) # adding amount is to ensure 

# Game loop
running  = True
while running:
    # looping all the available events in python
    screen.fill((0,0,0))
    # background image
    screen.blit(background, (0, 0))

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
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)

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

    # Enemy movement
    enemyX += enemyX_change

    if enemyX <= 0:
        enemyX_change = 0.3
        enemyY += enemyY_change # moving downwards when enemy hit the boudaries
    elif enemyX >= 736:
        enemyX_change = -0.3
        enemyY += enemyY_change

    # bullet movement
    if bulletY <= 0:
        bulletY = 400
        bullet_state = "ready"

    if bullet_state is "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    player(playerX, playerY)
    enemy(enemyX, enemyY)
    pygame.display.update() # we have to update the game window for any change in the code