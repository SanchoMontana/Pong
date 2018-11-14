import Pong


class Paddle:
    def __init__(self, x, y, height, girth, up, down):
        self.x = x
        self.y = y
        self.starting_height = height
        self.height = height
        self.girth = girth
        self.vel = 0
        self.starting_up = up
        self.starting_down = down
        self.move_up = up
        self.move_down = down

    def move(self):
        self.y += self.vel
        # Creates paddle boundaries.
        self.y = max(self.height / 2, self.y)
        self.y = min(Pong.DISPLAY_HEIGHT - self.height / 2, self.y)

    # Closes the gap between the two paddles.
    def enclose(self):
        if abs(self.x - Pong.DISPLAY_WIDTH / 2) > 100:  # If the paddles aren't too close to the center line.
            if self.x < Pong.DISPLAY_WIDTH / 2:
                self.x += 15
            else:
                self.x -= 15

    def reset(self):
        self.y = Pong.DISPLAY_HEIGHT / 2
        self.vel = 0
        self.height = self.starting_height  # This is here in case the paddles shrunk the previous round.
        self.move_up = self.starting_up
        self.move_down = self.starting_down
