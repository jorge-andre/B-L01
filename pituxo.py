# Example file showing a circle moving on screen
import pygame
import random

# pygame setup
pygame.init()

size = ()
screen = pygame.display.set_mode((410, 410), pygame.SCALED)
pygame.display.set_caption('Pituxo')

background = pygame.Surface(screen.get_size()).convert()
background.fill("purple")

clock = pygame.time.Clock()
dt = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

running = True
while running:
    # Process input
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update game state
    # fill the screen with a color to wipe away anything from last frame
    background.fill("purple")

    pygame.draw.circle(screen, "red", player_pos, 10)

    keys = pygame.key.get_pressed()
    
    mov_y = random.randint(-50,50) * dt
    mov_x = random.randint(-50,50) * dt

    if player_pos.y + mov_y in range (0, screen.get_height()):
        player_pos.y += mov_y 
    else:
        player_pos.y -= mov_y

    if player_pos.x + mov_x in range(0, screen.get_width()):
        player_pos.x += mov_x
    else:
        player_pos.x -= mov_x

    
    

    # Render graphics
    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()