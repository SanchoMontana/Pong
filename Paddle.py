import Pong

class Paddle:
    def __init__(self, x, y, height, girth):
        self.x = x
        self.y = y
        self.height = height
        self.girth = girth
        self.vel = 0

    def move(self):
        # TODO: set screen boundaries
        self.y += self.vel

        # Creates paddle boundaries.
        self.y = max(self.height / 2, self.y)
        self.y = min(Pong.DISPLAY_HEIGHT - self.height / 2, self.y)
        pass
    def shrink(self):
        pass

    def reset(self):
        self.y = Pong.DISPLAY_HEIGHT / 2
        self.vel = 0

