import Pong
from random import randint
from time import time
from math import sqrt


""" To add a powerUp, many things must be added:
    1. Add the color of the power up to the colors array, you should define the color first.
    2.change self.id to equal randint(1, <number of powerUps>)... Just add 1 to what it was before.
    2. Add the desired duration of the powerUp to the self.duration array.
    3. Write a class method for the powerUp that actually performs the powerUp.
        a. Preferably create a method with the arguments: class_method(self, ball, revert=False)
        b. Please use the increase_length(...) as a template for creating new powerUp methods.
    4. Add the class method to the self.method array.
"""


class PowerUp:

    def __init__(self, ball):
        RED = (255, 0, 0)
        BLUE = (0, 0, 255)
        GREEN = (0, 255, 0)
        YELLOW = (255, 255, 0)
        PURPLE = (255, 0, 255)
        colors = [RED, BLUE, GREEN, YELLOW, PURPLE]
        self.ballObj = ball
        self.radius = 15
        self.id = randint(0, 4)
        self.x = randint(Pong.DISPLAY_WIDTH / 2 - 100, Pong.DISPLAY_WIDTH / 2 + 100)
        self.y = randint(50, Pong.DISPLAY_HEIGHT - 50)
        self.color = colors[self.id]
        self.duration = [10, 10, 10, 10, 10]  # Seconds
        self.method = [self.increase_length, self.decrease_length, self.confuse, self.enlarge_ball, self.shrink_ball]
        self.start_time = None
        self.visibility = True
        self.affected_paddle = None
        self.active = False
        self.expired = False

    # PowerUp that increases the paddle length of the affected paddle.
    def increase_length(self, ball, revert=False):
        if not revert:
            if ball.last:
                self.affected_paddle = ball.last
                ball.last.height += 100
        else:
            if self.affected_paddle:
                self.affected_paddle.height -= 100
                self.expired = True

    # PowerUp that decreases the paddle length of the affected paddle.
    def decrease_length(self, ball, revert=False):
        if not revert:
            if ball.last:
                self.affected_paddle = ball.last
                ball.last.height -= 50
        else:
            if self.affected_paddle:
                self.affected_paddle.height += 50
                self.expired = True

    # PowerUp that switches a paddle's up and down keys.
    def confuse(self, ball, revert=False):
        if not revert:
            if ball.last:
                self.affected_paddle = ball.last
                temp = ball.last.move_up
                ball.last.move_up = ball.last.move_down
                ball.last.move_down = temp
        else:
            if self.affected_paddle:
                temp = self.affected_paddle.move_up
                self.affected_paddle.move_up = self.affected_paddle.move_down
                self.affected_paddle.move_down = temp
                self.expired = True

    # PowerUp that increases the ball size.
    def enlarge_ball(self, ball, revert=False):
        if not revert:
            if ball.last:
                ball.radius *= 2
        else:
            ball.radius /= 2
            self.expired = True

    # PowerUp that decreases the ball size.
    def shrink_ball(self, ball, revert=False):
        if not revert:
            if ball.last:
                ball.radius /= 2
        else:
            ball.radius *= 2
            self.expired = True

    # Checks if the ball makes contact with the powerUp.
    def check_passive(self, ball):
        if not self.active:
            # Checks if the ball and the PowerUp intersect.
            if sqrt((ball.x - self.x) ** 2 + (ball.y - self.y) ** 2) <= ball.radius + self.radius:  # TODO: Fix this.
                self.visibility = False
                self.start_time = int(time())
                self.method[self.id](ball)
                self.active = True

    # Checks if any active powers have been in play for its full duration, if so, the power is undone.
    def check_active(self, ball):
        if self.start_time:
            if int(time()) - self.start_time > self.duration[self.id]:
                self.method[self.id](ball, True)  # Reverts the change.
