from circleshape import CircleShape
import pygame
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
import random as r
from logger import log_event

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.x = x
        self.y = y
        self.radius = radius

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        random_angle = r.uniform(20, 50)
        new_asteroid_rot = self.velocity.rotate(random_angle)
        new_asteroid_rot2 = self.velocity.rotate(random_angle * -1)
        new_asteroid_radius = self.radius - ASTEROID_MIN_RADIUS
        new_asteroid = Asteroid(self.position[0], self.position[1], new_asteroid_radius)
        new_asteroid2 = Asteroid(self.position[0], self.position[1], new_asteroid_radius)
        new_asteroid.velocity = new_asteroid_rot * 1.2
        new_asteroid2.velocity = new_asteroid_rot2 * 1.2



        