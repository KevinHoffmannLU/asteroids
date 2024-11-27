import pygame
import random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
    def split(self):
        self.kill()
        
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            rand_angle = random.uniform(20, 50)
            asteroid_1_velocity = self.velocity.rotate(rand_angle)
            asteroid_2_velocity = self.velocity.rotate(-rand_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            asteroid_1 = Asteroid(self.position[0], self.position[1], new_radius)
            asteroid_2 = Asteroid(self.position[0], self.position[1], new_radius)
            asteroid_1.velocity = asteroid_1_velocity * 1.2
            asteroid_2.velocity = asteroid_2_velocity * 1.2
        
    def draw(self, screen):
        pygame.draw.circle(screen, 0xffffff, self.position, self.radius, 2)
        
    def update(self, dt):
        self.position += self.velocity * dt