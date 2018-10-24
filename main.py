import pygame

pygame.init()
pygame.mouse.set_visible(False)
DISPLAY_WIDTH = 1200
DISPLAY_HEIGHT = 800
gameDisplay = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
clock = pygame.time.Clock()

FPS = 50 # Frames per second.


game_exit = False

while not game_exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_exit = True  # This allows the X in the corner to close the window.
        elif event.type == pygame.KEYDOWN:  # Everything in this elif statement has key input handling
            pass
