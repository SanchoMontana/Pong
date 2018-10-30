import Pong
from random import randint
from time import time


class PowerUp:

    def __init__(self, ball):
        RED = (255, 0, 0)
        colors = [RED]
        self.ballObj = ball
        self.radius = 15
        self.id = randint(0, 0)
        self.x = randint(Pong.DISPLAY_WIDTH / 2 - 100, Pong.DISPLAY_WIDTH / 2 + 100)
        self.y = randint(50, Pong.DISPLAY_HEIGHT - 50)
        self.color = colors[self.id]
        self.start_time = None
        self.duration = [5]
        self.commands = [self.increase_length]
        self.revert = [self.increase_length]
        self.visibility = True
        self.affected_paddle = None
        self.active = False

    def increase_length(self, ball, revert=False):
        if not revert:
            if ball.last:
                self.affected_paddle = ball.last
                ball.last.height += 50
        else:
            if self.affected_paddle:
                self.affected_paddle.height -= 50
                del self

    def check_passive(self, ball):
        if not self.active:
            if ((ball.x - self.x) ** 2 + (ball.y - self.y) ** 2) ** 0.5 < ball.radius + self.radius:
                self.visibility = False
                self.start_time = int(time())
                self.commands[self.id](ball)
                self.active = True

    # Calculates if any active powers have been in play for its full duration, if so, the power is undone.
    def check_active(self, ball):
        if self.start_time:
            if int(time()) - self.start_time > self.duration[self.id]:
                self.revert[self.id](ball, True)
