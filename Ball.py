import Pong
import random


class Ball:
    def __init__(self, x, y, radius, x_vel, y_vel):
        self.x = x
        self.y = y
        self.radius = radius
        self.x_vel = x_vel
        self.y_vel = y_vel
        self.vel = (self.x_vel ** 2 + self.y_vel ** 2) ** 0.5
        self.tolerance = 5  # Allowing a collision if the center of the ball is just off the paddle
        self.hit_count = 0  # This will allow for the velocity of the ball to increase every 5 paddle hits.

    def move(self):

        # Simply changes the x and y componant of the ball according to its current velocity.
        self.x += self.x_vel
        self.y += self.y_vel

    def collision(self, p1, p2):
        # Collision detection with the upper and lower wall boundary.
        if self.y - self.radius < 0 or self.y + self.radius > Pong.DISPLAY_HEIGHT:
            self.y_vel *= -1
        
        # Main part of the collision detection with the paddle, firstly it check if the ball made contact with then it
        # splits the paddle into five imaginary sections and sees which section the ball made contact with. Lastly, the
        # y_vel is changed accordinly and the x_vel is changed to keep the same total velocity of the ball.
        # There is a little bit of randomness just so that the ball "should" never return to a perfectly straight path.
        
        if p1.y - p1.height / 2 - self.tolerance <= self.y <= p1.y + p1.height / 2 + self.tolerance:
            if self.x - self.radius <= p1.x + p1.girth / 2 <= self.x and self.x_vel < 0:
                p1_sections = [p1.y - p1.height / 2 - self.tolerance + ((p1.height + 2 * self.tolerance) / 5 * i)
                               for i in range(6)]
                if p1_sections[0] <= self.y <= p1_sections[1]:
                    self.y_vel -= self.vel * 0.2 + random.randint(-5, 5) * 0.01
                elif p1_sections[1] <= self.y <= p1_sections[2]:
                    self.y_vel -= self.vel * 0.1 + random.randint(-5, 5) * 0.01
                elif p1_sections[3] <= self.y <= p1_sections[4]:
                    self.y_vel += self.vel * 0.1 + random.randint(-5, 5) * 0.01
                elif p1_sections[4] <= self.y <= p1_sections[5]:
                    self.y_vel += self.vel * 0.2 + random.randint(-5, 5) * 0.01

                # This condition makes it so the y_vel doesnt get out of control
                if self.y_vel > 0:
                    self.y_vel = min(self.y_vel, 0.8 * self.vel)
                else:
                    self.y_vel = max(self.y_vel, -0.8 * self.vel)
                self.x_vel = (self.vel ** 2 - self.y_vel ** 2) ** 0.5

                # Increment hit count
                self.hit_count += 1

        if p2.y - p2.height / 2 - self.tolerance <= self.y <= p2.y + p2.height / 2 + self.tolerance:
            if self.x + self.radius >= p2.x - p2.girth / 2 >= self.x and self.x_vel > 0:
                p2_sections = [p2.y - p2.height / 2 - self.tolerance + ((p2.height + 2 * self.tolerance) / 5 * i) 
                               for i in range(6)]
                if p2_sections[0] <= self.y <= p2_sections[1]:
                    self.y_vel -= self.vel * 0.2 + random.randint(-5, 5) * 0.01
                elif p2_sections[1] <= self.y <= p2_sections[2]:
                    self.y_vel -= self.vel * 0.1 + random.randint(-5, 5) * 0.01
                elif p2_sections[3] <= self.y <= p2_sections[4]:
                    self.y_vel += self.vel * 0.1 + random.randint(-5, 5) * 0.01
                elif p2_sections[4] <= self.y <= p2_sections[5]:
                    self.y_vel += self.vel * 0.2 + random.randint(-5, 5) * 0.01

                if self.y_vel > 0:
                    self.y_vel = min(self.y_vel, 0.8 * self.vel)
                else:
                    self.y_vel = max(self.y_vel, -0.8 * self.vel)
                print("HELLLLLLO")
                self.x_vel = -((self.vel ** 2 - self.y_vel ** 2) ** 0.5)

                # Increment hit count
                self.hit_count += 1

        # Accelerates the ball every five contacts with a paddle.
        if self.hit_count >= 5:
            self.vel += 1
            self.hit_count = 0

    def goal(self):
        if self.x < -50 or self.x > Pong.DISPLAY_WIDTH + 50:
            return True
        else:
            return False

    def reset(self):
        self.x = Pong.DISPLAY_WIDTH / 2
        self.y = Pong.DISPLAY_HEIGHT / 2
        self.x_vel = 0
        self.y_vel = 0
        self.vel = 0
        self.hit_count = 0

