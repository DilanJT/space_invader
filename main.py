import pygame

# initialize the pygame
pygame.init()

#create the screen
screen = pygame.display.set_mode((800,600))

# Game loop
running  = True
while running:
    # looping all the available events in python
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False