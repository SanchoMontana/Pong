import pygame


if __name__ == '__main__':
    from Paddle import Paddle
    from Ball import Ball

DISPLAY_WIDTH = 1600
DISPLAY_HEIGHT = 800
PADDLE_GAP = 60
PADDLE_GIRTH = 20
PADDLE_SPEED = 8
BALL_RADIUS = 15
FPS = 80 # Frames per second.
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


pygame.init()
pygame.mouse.set_visible(False)
gameDisplay = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
clock = pygame.time.Clock()


def start_round(ball, velocity):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    ball.x_vel = velocity
                    ball.vel = abs(velocity)
                    return


def main():

    score = [0, 0]
    P1 = Paddle(PADDLE_GAP, DISPLAY_HEIGHT / 2, DISPLAY_HEIGHT / 4, PADDLE_GIRTH)
    P2 = Paddle(DISPLAY_WIDTH - PADDLE_GAP, DISPLAY_HEIGHT / 2, DISPLAY_HEIGHT / 4, PADDLE_GIRTH)
    ball = Ball(DISPLAY_WIDTH / 2, DISPLAY_HEIGHT / 2, BALL_RADIUS, 10, 0)
    game_exit = False

    def draw():
        # Updates the black background, everything that is drawn should be after this.
        gameDisplay.fill(BLACK)

        

        # Draws the middle line
        for i in range(20):
            pygame.draw.rect(gameDisplay, WHITE, [DISPLAY_WIDTH / 2 - 3, DISPLAY_HEIGHT / 20 * i, 6, DISPLAY_HEIGHT / 40])
        # Draw paddles
        pygame.draw.rect(gameDisplay, WHITE, [P1.x - P1.girth / 2, P1.y - P1.height / 2, P1.girth, P1.height])
        pygame.draw.rect(gameDisplay, WHITE, [P2.x - P2.girth / 2, P2.y - P1.height / 2, P2.girth, P2.height])
        # Draws the ball
        pygame.draw.circle(gameDisplay, WHITE, (int(ball.x), int(ball.y)), ball.radius)

        # Draws the score of each player on the top of the screen
        font = pygame.font.SysFont(None, 128)
        leftScoreText = font.render(str(score[0]), True, WHITE)
        gameDisplay.blit(leftScoreText, (DISPLAY_WIDTH / 2 - 75, 10))

        rightScoreText = font.render(str(score[1]), True, WHITE)
        gameDisplay.blit(rightScoreText, (DISPLAY_WIDTH / 2 + 25, 10))
        
        pygame.display.update()

        

    while not game_exit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit = True  # This allows the X in the corner to close the window.
            elif event.type == pygame.KEYDOWN:  # Everything in this elif statement has key input handling
                if event.key == pygame.K_w:
                    P1.vel -= PADDLE_SPEED
                elif event.key == pygame.K_s:
                    P1.vel += PADDLE_SPEED
                elif event.key == pygame.K_UP:
                    P2.vel -= PADDLE_SPEED
                elif event.key == pygame.K_DOWN:
                    P2.vel += PADDLE_SPEED
            elif event.type == pygame.KEYUP:  # Event handling when key is lifted.
                if event.key == pygame.K_w:
                    P1.vel += PADDLE_SPEED
                elif event.key == pygame.K_s:
                    P1.vel -= PADDLE_SPEED
                elif event.key == pygame.K_UP:
                    P2.vel += PADDLE_SPEED
                elif event.key == pygame.K_DOWN:
                    P2.vel -= PADDLE_SPEED

        # Move Paddles and Ball
        P1.move()
        P2.move()
        ball.move()
        ball.collision(P1, P2)

        # Check if there is a goal
        if ball.goal():
            P1.reset()
            P2.reset()

            # Checks which player scored, increases their score and gives them the ball to start the next round
            if ball.x > DISPLAY_WIDTH:
                ball.reset()
                score = [score[0] + 1, score[1]]
                draw()
                start_round(ball, 10)
            else:
                ball.reset()
                score = [score[0], score[1] + 1]
                draw()
                start_round(ball, -10)
            if score[0] >= 5 or score [1] >=  5:
                # Win condition
                # Todo: Display that player 1 or 2 wins then give them an option to play again.
                
                pygame.quit()
                quit()

        # Update the game
        draw()
        clock.tick(FPS)

    pygame.quit()
    quit()


if __name__ == '__main__':
    main()

