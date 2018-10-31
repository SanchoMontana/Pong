import Pong


class Paddle:
    def __init__(self, x, y, height, girth):
        self.x = x
        self.y = y
        self.starting_height = height
        self.height = height
        self.girth = girth
        self.vel = 0

    def move(self):
        self.y += self.vel
        # Creates paddle boundaries.
        self.y = max(self.height / 2, self.y)
        self.y = min(Pong.DISPLAY_HEIGHT - self.height / 2, self.y)

    # Closes the gap between the two paddles.
    def enclose(self):
        if abs(self.x - Pong.DISPLAY_WIDTH) > 100:  # If the paddles aren't too close to the center line.
            if self.x < Pong.DISPLAY_WIDTH / 2:
                self.x += 15
            else:
                self.x -= 15

    def reset(self):
        self.y = Pong.DISPLAY_HEIGHT / 2
        self.vel = 0
        self.height = self.starting_height  # This is here in case the paddles shrunk the previous round.
