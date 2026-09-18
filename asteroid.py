from circleshape import CircleShape
import pygame
from constants import LINE_WIDTH

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.x = x
        self.y = y
        self.radius = radius
        self.center = [x, y]

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.center, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.center = self.center + (self.velocity * dt)
        print(self.velocity)