import pygame
from time import sleep, time


if __name__ == '__main__':
    from Paddle import Paddle
    from Ball import Ball
    from PowerUp import PowerUp

DISPLAY_WIDTH = 1200
DISPLAY_HEIGHT = 700
PADDLE_GAP = 60
PADDLE_GIRTH = 20
PADDLE_SPEED = 8
BALL_RADIUS = 15
BALL_START_VEL = 10
FPS = 80  # Frames per second.
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
SCORE_TO_WIN = 5
START_TIME = int(time())  # This is used for creating powerUps.


pygame.init()
pygame.mouse.set_visible(False)
gameDisplay = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
clock = pygame.time.Clock()
score_font = pygame.font.SysFont(None, DISPLAY_WIDTH // 20)
alert_font = pygame.font.SysFont(None, 24)


# Waits until the user is ready to start the next round.
def start_round(ball, velocity):
    alert = alert_font.render("Press [space] to continue", True, WHITE)
    pygame.draw.rect(gameDisplay, BLACK,
                     [DISPLAY_WIDTH // 2 - alert.get_width() // 2,
                      DISPLAY_HEIGHT - 2 * alert.get_height() - 15,
                      alert.get_width(), alert.get_height() * 2])
    gameDisplay.blit(alert, (DISPLAY_WIDTH // 2 - alert.get_width() // 2, DISPLAY_HEIGHT - alert.get_height() - 15))
    pygame.display.update()
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

    def draw():
        # Updates the black background, everything that is drawn should be after this.
        gameDisplay.fill(BLACK)

        # Draws the middle line
        for i in range(20):
            pygame.draw.rect(gameDisplay, WHITE,
                             [DISPLAY_WIDTH / 2 - 3, DISPLAY_HEIGHT / 20 * i, 6, DISPLAY_HEIGHT / 40])
        # Draw paddles
        pygame.draw.rect(gameDisplay, WHITE, [P1.x - P1.girth / 2, P1.y - P1.height / 2, P1.girth, P1.height])
        pygame.draw.rect(gameDisplay, WHITE, [P2.x - P2.girth / 2, P2.y - P2.height / 2, P2.girth, P2.height])
        # Draws the ball
        pygame.draw.circle(gameDisplay, WHITE, (int(ball.x), int(ball.y)), ball.radius)

        # Draws powerUps
        for i in power:
            if i.visibility:
                pygame.draw.circle(gameDisplay, i.color, (i.x, i.y), 30)

        # Draws the score of each player on the top of the screen
        leftScoreText = score_font.render(str(score[0]), True, WHITE)
        gameDisplay.blit(leftScoreText, (DISPLAY_WIDTH / 2 - leftScoreText.get_width() - 20, 10))

        rightScoreText = score_font.render(str(score[1]), True, WHITE)
        gameDisplay.blit(rightScoreText, (DISPLAY_WIDTH / 2 + 20, 10))
        
        pygame.display.update()

    # Checks if one player reached the winning score. If so, it displays the winner and restarts the game.
    def end_of_game(scores):
        if scores[0] >= SCORE_TO_WIN or scores[1] >= SCORE_TO_WIN:
            draw()
            # Win condition
            if scores[0] >= SCORE_TO_WIN:
                winner = score_font.render("Left Paddle Wins!", True, WHITE)
            else:
                winner = score_font.render("Right Paddle Wins!", True, WHITE)

            pygame.draw.rect(gameDisplay, BLACK,
                             [DISPLAY_WIDTH / 2 - winner.get_width() / 2,
                              DISPLAY_HEIGHT / 2 - winner.get_height() / 2 - 20,
                              winner.get_width(), winner.get_height() + 40])
            gameDisplay.blit(winner,
                             (DISPLAY_WIDTH / 2 - winner.get_width() / 2,
                              DISPLAY_HEIGHT / 2 - winner.get_height() / 2))
            pygame.display.update()
            sleep(2)
            alert = alert_font.render("Press [space] to play again or [esc] to quit.", True, WHITE)
            pygame.draw.rect(gameDisplay, BLACK,
                             [DISPLAY_WIDTH // 2 - alert.get_width() // 2,
                              DISPLAY_HEIGHT - 2 * alert.get_height() - 15,
                              alert.get_width(), alert.get_height() * 2])
            gameDisplay.blit(alert, (DISPLAY_WIDTH // 2 - alert.get_width() // 2,
                                     DISPLAY_HEIGHT - alert.get_height() - 15))
            pygame.display.update()
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            return [0, 0]
                        if event.key == pygame.K_ESCAPE:
                            pygame.quit()
                            quit()
        return scores

    score = [0, 0]
    P1 = Paddle(PADDLE_GAP, DISPLAY_HEIGHT / 2,
                DISPLAY_HEIGHT / 4, PADDLE_GIRTH, pygame.K_w, pygame.K_s)
    P2 = Paddle(DISPLAY_WIDTH - PADDLE_GAP, DISPLAY_HEIGHT / 2,
                DISPLAY_HEIGHT / 4, PADDLE_GIRTH, pygame.K_UP, pygame.K_DOWN)
    ball = Ball(DISPLAY_WIDTH / 2, DISPLAY_HEIGHT / 2, BALL_RADIUS, BALL_START_VEL, 0)
    game_exit = False  # Exits the main loop if this is True.
    add_power = int(time())
    power = []  # Will be appended every x seconds.

    # Input Handing loop
    while not game_exit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit = True  # This allows the X in the corner to close the window.
            elif event.type == pygame.KEYDOWN:  # Everything in this elif statement has key input handling
                if event.key == P1.move_up:
                    P1.vel -= PADDLE_SPEED
                elif event.key == P1.move_down:
                    P1.vel += PADDLE_SPEED
                elif event.key == P2.move_up:
                    P2.vel -= PADDLE_SPEED
                elif event.key == P2.move_down:
                    P2.vel += PADDLE_SPEED
            elif event.type == pygame.KEYUP:  # Event handling when key is lifted.
                if event.key == P1.move_up:
                    P1.vel += PADDLE_SPEED
                elif event.key == P1.move_down:
                    P1.vel -= PADDLE_SPEED
                elif event.key == P2.move_up:
                    P2.vel += PADDLE_SPEED
                elif event.key == P2.move_down:
                    P2.vel -= PADDLE_SPEED

        # Move Paddles and Ball
        P1.move()
        P2.move()
        ball.move()
        ball.collision(P1, P2)

        # Create PowerUp every ten seconds
        if (int(time()) - START_TIME) % 10 == 0:
            if add_power != int(time()):
                power.append(PowerUp(ball))
                add_power = int(time())

        # Check ball Collision with PowerUps
        for i in power:
            i.check_passive(ball)
            i.check_active(ball)
            if i.expired:
                power.remove(i)

        # Check if there is a goal
        if ball.goal():
            P1.reset()
            P2.reset()
            if ball.x > DISPLAY_WIDTH:
                score = [score[0] + 1, score[1]]
            else:
                score = [score[0], score[1] + 1]
            score = end_of_game(score)

            # Checks which player scored, increases their score and gives them the ball to start the next round
            if ball.x > DISPLAY_WIDTH:
                ball.reset()
                draw()
                start_round(ball, 10)
            else:
                ball.reset()
                draw()
                start_round(ball, -10)
            power = []  # Clears the arena of any unused powerUps.

        # Update the game
        draw()
        clock.tick(FPS)

    pygame.quit()
    quit()


if __name__ == '__main__':
    main()
