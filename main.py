import pygame
from Paddle import Paddle
from Ball import Ball

pygame.init()
pygame.mouse.set_visible(False)
DISPLAY_WIDTH = 1200
DISPLAY_HEIGHT = 800
gameDisplay = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
clock = pygame.time.Clock()

FPS = 50 # Frames per second.

WHITE = (255, 255, 255)

P1 = Paddle(50, DISPLAY_HEIGHT / 2, DISPLAY_HEIGHT / 5, 0)
P2 = Paddle(1150, DISPLAY_HEIGHT / 2, DISPLAY_HEIGHT / 5, 0)


game_exit = False

while not game_exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_exit = True  # This allows the X in the corner to close the window.
        elif event.type == pygame.KEYDOWN:  # Everything in this elif statement has key input handling
            pass

    #Draw Player 1s paddle
    pygame.draw.rect(gameDisplay, WHITE, [P1.x - P1.girth / 2, P1.y - P1.height / 2, P1.girth, P1.height])

    #Draw Player 2s paddle
    pygame.draw.rect(gameDisplay, WHITE, [P2.x - P2.girth / 2, P2.y - P1.height / 2, P2.girth, P2.height])

    #Update the game
    pygame.display.update()
    clock.tick(FPS)
    
