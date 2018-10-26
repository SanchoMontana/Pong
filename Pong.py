import pygame


if __name__ == '__main__':
    from Paddle import Paddle
    from Ball import Ball

DISPLAY_WIDTH = 1600
DISPLAY_HEIGHT = 800
PADDLE_GAP = 60
PADDLE_GIRTH = 20
BALL_RADIUS = 15
FPS = 80 # Frames per second.
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


pygame.init()
pygame.mouse.set_visible(False)
gameDisplay = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
clock = pygame.time.Clock()

def main():

    P1 = Paddle(PADDLE_GAP, DISPLAY_HEIGHT / 2, DISPLAY_HEIGHT / 4, PADDLE_GIRTH, 0)
    P2 = Paddle(DISPLAY_WIDTH - PADDLE_GAP, DISPLAY_HEIGHT / 2, DISPLAY_HEIGHT / 4, PADDLE_GIRTH, 0)
    ball = Ball(DISPLAY_WIDTH / 2, DISPLAY_HEIGHT / 2, BALL_RADIUS, 10, 0)
    game_exit = False
    while not game_exit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit = True  # This allows the X in the corner to close the window.
            elif event.type == pygame.KEYDOWN:  # Everything in this elif statement has key input handling
                if event.key == pygame.K_w:
                    P1.vel -= 6
                elif event.key == pygame.K_s:
                    P1.vel += 6
                elif event.key == pygame.K_UP:
                    P2.vel -= 6
                elif event.key == pygame.K_DOWN:
                    P2.vel += 6
            elif event.type == pygame.KEYUP:  # Event handling when key is lifted.
                if event.key == pygame.K_w:
                    P1.vel += 6
                elif event.key == pygame.K_s:
                    P1.vel -= 6
                elif event.key == pygame.K_UP:
                    P2.vel += 6
                elif event.key == pygame.K_DOWN:
                    P2.vel -= 6

        # Move Paddles and Ball
        P1.move()
        P2.move()
        ball.move()
        ball.collision(P1, P2)

        # Updates the black background, everything that is drawn should be after this.
        gameDisplay.fill(BLACK)
        # Draw paddles
        pygame.draw.rect(gameDisplay, WHITE, [P1.x - P1.girth / 2, P1.y - P1.height / 2, P1.girth, P1.height])
        pygame.draw.rect(gameDisplay, WHITE, [P2.x - P2.girth / 2, P2.y - P1.height / 2, P2.girth, P2.height])
        # Draws the ball
        pygame.draw.circle(gameDisplay, WHITE, (int(ball.x), int(ball.y)), ball.radius)
        # Update the game
        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()
    quit()


if __name__ == '__main__':
    main()

