import random

import pygame

from circleshape import CircleShape
from constants import *
from logger import log_event

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        random_angle = random.uniform(20, 50)
        first_child_vector = self.velocity.rotate(random_angle)
        second_child_vector = self.velocity.rotate(0-random_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        first_child = Asteroid(self.position.x, self.position.y, new_radius)
        second_child = Asteroid(self.position.x, self.position.y, new_radius)
        first_child.velocity = first_child_vector * 1.2
        second_child.velocity = second_child_vector * 1.2
