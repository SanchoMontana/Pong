import Pong

class Ball:
    def __init__(self, x, y, radius, x_vel, y_vel):
        self.x = x
        self.y = y
        self.radius = radius
        self.x_vel = x_vel
        self.y_vel = y_vel
        self.vel = (self.x_vel ** 2 + self.y_vel ** 2) ** 0.5
        self.tolerance = 5  # Allowing a collision if the center of the ball is just off the paddle

    def move(self):
        self.x += self.x_vel
        self.y += self.y_vel

    def collision(self, P1, P2):
        if self.y - self.radius < 0 or self.y  + self.radius > Pong.DISPLAY_HEIGHT:
            self.y_vel *= -1

        if P1.y - P1.height / 2 - self.tolerance <= self.y <= P1.y + P1.height / 2 + self.tolerance:
            if self.x - self.radius <= P1.x + P1.girth / 2 <= self.x and self.x_vel < 0:
                P1_array = [P1.y - P1.height / 2 - self.tolerance + ((P1.height + 2 * self.tolerance) / 5 * i) for i in range(6)]
                if P1_array[0] <= self.y <= P1_array[1]:
                    self.y_vel -= self.vel / 2 - self.y_vel / 2
                    self.x_vel = (self.vel ** 2 - self.y_vel ** 2) ** 0.5
                elif P1_array[1] <= self.y <= P1_array[2]:
                    self.y_vel -= self.vel / 3 - self.y_vel / 3
                    self.x_vel = (self.vel ** 2 - self.y_vel ** 2) ** 0.5
                elif P1_array[2] <= self.y <= P1_array[3]:
                    self.x_vel = (self.vel ** 2 - self.y_vel ** 2) ** 0.5
                elif P1_array[3] <= self.y <= P1_array[4]:
                    self.y_vel += self.vel / 3 - self.y_vel / 3
                    self.x_vel = (self.vel ** 2 - self.y_vel ** 2) ** 0.5
                elif P1_array[4] <= self.y <= P1_array[5]:
                    self.y_vel += self.vel / 2 - self.y_vel / 2
                    self.x_vel = (self.vel ** 2 - self.y_vel ** 2) ** 0.5

        if P2.y - P2.height / 2 - self.tolerance <= self.y <= P2.y + P2.height / 2 + self.tolerance:
            if self.x + self.radius >= P2.x - P2.girth / 2 >= self.x and self.x_vel > 0:
                P2_array = [P2.y - P2.height / 2 - self.tolerance + ((P2.height + 2 * self.tolerance) / 5 * i) for i in range(6)]
                if P2_array[0] <= self.y <= P2_array[1]:
                    self.y_vel -= self.vel / 2 - self.y_vel / 2
                    self.x_vel = -((self.vel ** 2 - self.y_vel ** 2) ** 0.5)
                elif P2_array[1] <= self.y <= P2_array[2]:
                    self.y_vel -= self.vel / 3 - self.y_vel / 3
                    self.x_vel = -((self.vel ** 2 - self.y_vel ** 2) ** 0.5)
                elif P2_array[2] <= self.y <= P2_array[3]:
                    self.x_vel = -((self.vel ** 2 - self.y_vel ** 2) ** 0.5)
                elif P2_array[3] <= self.y <= P2_array[4]:
                    self.y_vel += self.vel / 3 - self.y_vel / 3
                    self.x_vel = -((self.vel ** 2 - self.y_vel ** 2) ** 0.5)
                elif P2_array[4] <= self.y <= P2_array[5]:
                    self.y_vel += self.vel / 2 - self.y_vel / 2
                    self.x_vel = -((self.vel ** 2 - self.y_vel ** 2) ** 0.5)

